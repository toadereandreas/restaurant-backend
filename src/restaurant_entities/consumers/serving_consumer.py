import json
from channels.generic.websocket import AsyncWebsocketConsumer
from ..signals.serving import connect_serving
from asgiref.sync import sync_to_async

class ServingConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.waiter = self.scope['url_route']['kwargs']['waiter']
        self.room_group_name = 'serving_%s' % self.waiter

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()
        await sync_to_async(connect_serving.send)(sender=self.__class__, pk=self.waiter)

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        data = text_data_json['data']

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'send_servings',
                'data': data
            }
        )


    async def send_servings(self, event):

        with open('log_receiver.txt', 'a') as f:
            f.write('serving_consumer - Send to websocket:\n\tdata: %s\n' % event['data'])

        # Send servings to web socket
        await self.send(text_data=event['data'])
