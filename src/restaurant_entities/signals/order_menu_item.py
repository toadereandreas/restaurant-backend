from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from ..models.order.order_menu_item import OrderMenuItem
import json
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


@receiver([post_save, post_delete], sender=OrderMenuItem)
def send_to_order_menu_item_consumer(sender, instance, **kwargs):
    room_group_name = "order_menu_item_" + str(instance.order.serving.user.pk)

    qs = OrderMenuItem.objects.filter(order__serving__user=instance.order.serving.user)
    data = order_menu_items_to_json(qs)
    
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
