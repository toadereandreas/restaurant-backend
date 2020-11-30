from django.db import models
from ..base import GlobalID
from ..menu.menu_item import MenuItem
from .order import Order


class OrderMenuItem(GlobalID, models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField()
