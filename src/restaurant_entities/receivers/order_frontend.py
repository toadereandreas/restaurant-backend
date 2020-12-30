from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from ..models.order.order import Order
from ..signals.order_frontend import connect_order_frontend
from ..consumers.order_consumer_frontend import OrderFrontendConsumer
import json
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


def send_orders_frontend(data, room_group_name):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        room_group_name,
        {
            'type': 'send_orders_frontend',
            'data': data
        }
    )


def orders_frontend_to_json(qs):
    order_list = []
    for order in qs:
        order_list.append({
                "id": str(order.id),
                "note": order.note,
                "locked": order.locked,
            })
    if OrderFrontendConsumer.order_list_final != order_list:
        OrderFrontendConsumer.order_list_final = order_list
        return json.dumps(order_list)
    OrderFrontendConsumer.order_list_final = order_list
    return []


@receiver(connect_order_frontend, sender=OrderFrontendConsumer)
def send_to_order_frontend_consumer_on_connect(sender, pk, **kwargs):
    OrderFrontendConsumer.order_list_final = []

    room_group_name = "order_frontend_%s" % str(pk)

    qs = Order.objects.filter(id=pk)
    data = orders_frontend_to_json(qs)

    send_orders_frontend(data, room_group_name)


@receiver([post_save, post_delete], sender=Order)
def send_to_order_frontend_consumer(sender, instance, **kwargs):
    room_group_name = "order_frontend_%s" % str(instance.id)

    qs = Order.objects.filter(id=instance.id)
    
    # in exclude also add field "locked"
    data = orders_frontend_to_json(qs)
    send_orders_frontend(data, room_group_name)
