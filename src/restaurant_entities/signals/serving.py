from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from ..models.order.serving import Serving
import json
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


@receiver([post_save, post_delete], sender=Serving)
def send_to_serving_consumer(sender, instance, **kwargs):
    room_group_name = "serving_" + str(instance.user.pk)

    qs = Serving.objects.filter(user=instance.user)
    data = servings_to_json(qs)
    
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
                "call": False,
                "code": serving.code,
                "name": serving.name,
                "tableId": str(serving.gid)
            })

    return json.dumps(serving_list)
