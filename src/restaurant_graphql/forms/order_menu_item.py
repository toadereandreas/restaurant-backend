from restaurant_entities.models.order import OrderMenuItem
from django.core.exceptions import ValidationError
from .base import BaseForm


class OrderMenuItemForm(BaseForm):
    class Meta:
        model = OrderMenuItem
        fields = [
            'menu_item',
            'order',
            'quantity'
        ]
