from restaurant_entities.models.menu import MenuItemTranslation
from django.core.exceptions import ValidationError
from .base import BaseForm


class MenuItemTranslationForm(BaseForm):
    class Meta:
        model = MenuItemTranslation
        fields = [
            'menu_item',
            'language',
            'name',
            'description',
            'quantity'
        ]
