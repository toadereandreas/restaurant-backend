from restaurant_entities.models.menu import Allergen
from django.core.exceptions import ValidationError
from .base import BaseForm


class AllergenForm(BaseForm):
    class Meta:
        model = Allergen
        fields = [
            'number'
        ]
