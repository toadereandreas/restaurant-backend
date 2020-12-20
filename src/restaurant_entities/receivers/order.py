from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from ..models.order.order import Order
from ..signals.order import connect_order
from ..consumers.order_consumer import OrderConsumer
import json
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


def send_orders(data, room_group_name):
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

@receiver(connect_order, sender=OrderConsumer)
def send_to_order_consumer_on_connect(sender, pk, **kwargs):
    room_group_name = "order_%s" % str(pk)

    qs = Order.objects.filter(serving__user__pk=pk)
    data = orders_to_json(qs)

    send_orders(data, room_group_name)

@receiver([post_save, post_delete], sender=Order)
def send_to_order_consumer(sender, instance, **kwargs):
    room_group_name = "order_%s" % str(instance.serving.user.pk)

    qs = Order.objects.filter(serving__user=instance.serving.user)
    data = orders_to_json(qs)

    send_orders(data, room_group_name)
