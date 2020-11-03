from restaurant_entities.models.menu import Language
from django.core.exceptions import ValidationError
from .base import BaseForm


class LanguageForm(BaseForm):
    class Meta:
        model = Language
        fields = [
            'name',
            'code',
        ]
