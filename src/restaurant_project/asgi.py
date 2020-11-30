"""
ASGI config for restaurant project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os
import django
from django.core.asgi import get_asgi_application
from django.urls import path 
from channels.routing import ProtocolTypeRouter, URLRouter

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'restaurant_project.settings.base')
django.setup()

from graphene_subscriptions.consumers import GraphqlSubscriptionConsumer


class CustomProtocolTypeRouter(ProtocolTypeRouter):
    """
    Overrided base class's __call__ method to support python socketio 4.2.0 and daphne 2.3.0
    """
    def __call__(self, scope, *args):
        if scope["type"] in self.application_mapping:
            handlerobj = self.application_mapping[scope["type"]](scope)
            if args:
                return handlerobj(*args)
            return handlerobj
        raise ValueError(
            "No application configured for scope type %r" % scope["type"]
        )


application = CustomProtocolTypeRouter({
     "websocket": URLRouter([
        path('graphql/', GraphqlSubscriptionConsumer)
    ]),
})
