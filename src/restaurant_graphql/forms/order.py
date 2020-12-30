from restaurant_entities.models.order import Order
from django.core.exceptions import ValidationError
from .base import BaseForm
from django import forms


class OrderForm(BaseForm):
    class Meta:
        model = Order
        fields = [
            'serving',
            'color',
            'note',
            'locked',
        ]

    # serving = forms.UUIDField(required=True)
