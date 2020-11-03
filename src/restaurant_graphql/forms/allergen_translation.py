from restaurant_entities.models.menu import AllergenTranslation
from django.core.exceptions import ValidationError
from .base import BaseForm


class AllergenTranslationForm(BaseForm):
    class Meta:
        model = AllergenTranslation
        fields = [
            'name',
            'allergen',
            'language'
        ]
