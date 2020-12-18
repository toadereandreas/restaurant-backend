from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from ..models.order.order import Order
import json
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


@receiver([post_save, post_delete], sender=Order)
def send_to_order_consumer(sender, instance, **kwargs):
    room_group_name = "order_" + str(instance.serving.user.pk)

    qs = Order.objects.filter(serving__user=instance.serving.user)
    data = orders_to_json(qs)
    
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        room_group_name,
        {
            'type': 'send_orders',
            'data': data
        }
    )

def orders_to_json(qs):
    order_list = []
    for order in qs:
        order_list.append({
                "note": order.note,
                "orderColor": order.color,
                "tableId": str(order.serving.gid)
            })

    return json.dumps(order_list)
