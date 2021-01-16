from restaurant_entities.models.order import OrderMenuItem, Order
from restaurant_entities.models.menu.menu_item import MenuItem

from django.core.exceptions import ValidationError
from .base import BaseForm
from django import forms


class OrderMenuItemForm(BaseForm):
    class Meta:
        model = OrderMenuItem
        fields = [
            'menu_item',
            'order',
            'quantity'
        ]

    menu_item = forms.UUIDField(required=True)
    order = forms.UUIDField(required=True)

    def clean_menu_item(self):
        gid = self.cleaned_data.get('menu_item')
        menu_item = MenuItem.objects.get(gid=gid)
        if not menu_item:
            raise ValidationError(
                "Menu Item does not exist."
            )
        return menu_item

    def clean_order(self):
        gid = self.cleaned_data.get('order')
        order = Order.objects.get(gid=gid)
        if not order:
            raise ValidationError(
                "Order does not exist."
            )
        return order

    def clean(self):
        super().clean()
