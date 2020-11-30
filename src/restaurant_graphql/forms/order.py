from restaurant_entities.models.order import Order
from django.core.exceptions import ValidationError
from .base import BaseForm


class OrderForm(BaseForm):
    class Meta:
        model = Order
        fields = [
            'serving',
            'color',
            'note'
        ]
