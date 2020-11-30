from django.db.models.signals import post_save, post_delete
from graphene_subscriptions.signals import post_save_subscription, post_delete_subscription

from restaurant_entities.models.order import Serving

post_save.connect(post_save_subscription, sender=Serving, dispatch_uid="serving_post_save")
post_delete.connect(post_delete_subscription, sender=Serving, dispatch_uid="serving_post_delete")
