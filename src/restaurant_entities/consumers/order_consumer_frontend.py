import json
from channels.generic.websocket import AsyncWebsocketConsumer
from ..signals.order_frontend import connect_order_frontend
from asgiref.sync import sync_to_async


class OrderFrontendConsumer(AsyncWebsocketConsumer):
    order_list_final = []

    async def connect(self):
        self.waiter = self.scope['url_route']['kwargs']['id']
        self.room_group_name = 'order_frontend_%s' % self.waiter

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()
        await sync_to_async(connect_order_frontend.send)(sender=self.__class__, pk=self.waiter)

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
                'type': 'send_orders_frontend',
                'data': data
            }
        )


    async def send_orders_frontend(self, event):
        await self.send(text_data=event['data'])
