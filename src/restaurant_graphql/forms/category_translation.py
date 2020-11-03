from restaurant_entities.models.menu import CategoryTranslation
from django.core.exceptions import ValidationError
from .base import BaseForm


class CategoryTranslationForm(BaseForm):
    class Meta:
        model = CategoryTranslation
        fields = [
            'category',
            'language',
            'name'
        ]
