from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from ..models.order.order import Order
from ..signals.order_frontend import connect_order_frontend
from ..consumers.order_consumer_frontend import OrderFrontendConsumer
import json
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

# class Ss:
#
#     @staticmethod
def send_orders_frontend(data, room_group_name):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        room_group_name,
        {
            'type': 'send_orders_frontend',
            'data': data
        }
    )
order_list_final=[]

def orders_frontend_to_json(qs):
    order_list = []
    for order in qs:
        order_list.append({
                "gid": str(order.gid),
                "note": order.note,
                "locked": "true",
            })
    global order_list_final
    if order_list_final != order_list:
        order_list_final = order_list
        return json.dumps(order_list)
    order_list_final = order_list
    return []
    # return json.dumps(order_list)

@receiver(connect_order_frontend, sender=OrderFrontendConsumer)
def send_to_order_frontend_consumer_on_connect(sender, pk, **kwargs):
    room_group_name = "order_frontend_%s" % str(pk)

    # qs = Order.objects.filter(serving__user__pk=pk)
    qs = Order.objects.filter(gid=pk)
    data = orders_frontend_to_json(qs)

    send_orders_frontend(data, room_group_name)

@receiver([post_save, post_delete], sender=Order)
def send_to_order_frontend_consumer(sender, instance, **kwargs):
    room_group_name = "order_frontend_%s" % str(instance.gid)

    # qs = Order.objects.filter(serving__user=instance.serving.user)
    qs = Order.objects.filter(gid=instance.gid)
    # in exclude also add field "locked"
    # qs = Order.objects.exclude(note=instance.note)
    data = orders_frontend_to_json(qs)

    send_orders_frontend(data, room_group_name)
