"""restaurant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from restaurant_entities.consumers import ChatConsumer, ServingConsumer, OrderConsumer, OrderFrontendConsumer, OrderMenuItemConsumer

websocket_urlpatterns = [
    path('ws/chat/<room_name>/', ChatConsumer.as_asgi()),
    path('ws/serving/<int:waiter>/', ServingConsumer.as_asgi()),
    path('ws/order/<int:waiter>/', OrderConsumer.as_asgi()),
    path('ws/orderfrontend/<gid>/', OrderFrontendConsumer.as_asgi()),
    path('ws/ordermenuitem/<int:waiter>/', OrderMenuItemConsumer.as_asgi()),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
]

