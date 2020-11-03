from restaurant_entities.models.menu import Category
from django.core.exceptions import ValidationError
from .base import BaseForm


class CategoryForm(BaseForm):
    class Meta:
        model = Category
        fields = [
            'internal_name'
        ]

