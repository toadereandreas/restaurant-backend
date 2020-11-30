from django.db.models.signals import post_save, post_delete
from graphene_subscriptions.signals import post_save_subscription, post_delete_subscription

from restaurant_entities.models.order import Order

post_save.connect(post_save_subscription, sender=Order, dispatch_uid="order_post_save")
post_delete.connect(post_delete_subscription, sender=Order, dispatch_uid="order_post_delete")
