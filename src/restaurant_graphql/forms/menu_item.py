from restaurant_entities.models.menu import MenuItem
from django.core.exceptions import ValidationError
from .base import BaseForm


class MenuItemForm(BaseForm):
    class Meta:
        model = MenuItem
        fields = [
            'internal_name',
            'picture',
            'price',
            'allergens'
        ]
