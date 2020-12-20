from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from ..models.order.order_menu_item import OrderMenuItem
from ..signals.order_menu_item import connect_order_menu_item
from ..consumers.order_menu_item_consumer import OrderMenuItemConsumer
import json
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


def send_order_menu_items(data, room_group_name):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        room_group_name,
        {
            'type': 'send_order_menu_items',
            'data': data
        }
    )

def order_menu_items_to_json(qs):
    order_menu_item_list = []
    for item in qs:
        order_menu_item_list.append({
                "menuItemId": str(item.menu_item.gid),
                "orderColor": item.order.color,
                "quantity": item.quantity,
                "tableId": str(item.order.serving.gid)
            })

    return json.dumps(order_menu_item_list)

@receiver(connect_order_menu_item, sender=OrderMenuItemConsumer)
def send_to_order_menu_item_consumer_on_connect(sender, pk, **kwargs):
    room_group_name = "order_menu_item_%s" % str(pk)

    qs = OrderMenuItem.objects.filter(order__serving__user__pk=pk)
    data = order_menu_items_to_json(qs)
    
    send_order_menu_items(data, room_group_name)

@receiver([post_save, post_delete], sender=OrderMenuItem)
def send_to_order_menu_item_consumer(sender, instance, **kwargs):
    room_group_name = "order_menu_item_%s" % str(instance.order.serving.user.pk)

    qs = OrderMenuItem.objects.filter(order__serving__user=instance.order.serving.user)
    data = order_menu_items_to_json(qs)
    
    send_order_menu_items(data, room_group_name)
