from django.db.models.signals import post_save, post_delete
from graphene_subscriptions.signals import post_save_subscription, post_delete_subscription

from restaurant_entities.models import Table

post_save.connect(post_save_subscription, sender=Table, dispatch_uid="table_post_save")
post_delete.connect(post_delete_subscription, sender=Table, dispatch_uid="table_post_delete")
