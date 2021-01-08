from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from ..models.order.serving import Serving
from ..signals.serving import connect_serving
from ..consumers.serving_consumer import ServingConsumer
import json
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

def send_servings(data, room_group_name):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        room_group_name,
        {
            'type': 'send_servings',
            'data': data
        }
    )

def servings_to_json(qs):
    serving_list = []
    for serving in qs:
        serving_list.append({
                "call": serving.called,
                "code": serving.code,
                "name": serving.name,
                "tableId": str(serving.gid)
            })

    return json.dumps(serving_list)

@receiver(connect_serving, sender=ServingConsumer)
def send_to_serving_consumer_on_connect(sender, pk, **kwargs):
    room_group_name = "serving_%s" % str(pk)

    qs = Serving.objects.filter(user__pk=pk)
    data = servings_to_json(qs)

    with open('log_receiver.txt', 'a') as f:
        f.write('connect_serving receiver:\n\tsendig to room: %s\n\tdata: %s\n' % (room_group_name, data) )

    send_servings(data, room_group_name)

@receiver([post_save, post_delete], sender=Serving)
def send_to_serving_consumer(sender, instance, **kwargs):
    room_group_name = "serving_%s" % str(instance.user.pk)

    qs = Serving.objects.filter(user=instance.user)
    data = servings_to_json(qs)
    
    with open('log_receiver.txt', 'a') as f:
        f.write('post_save/delete receiver:\n\tsendig to room: %s\n\tdata: %s\n' % (room_group_name, data) )

    send_servings(data, room_group_name)
