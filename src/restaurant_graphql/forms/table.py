from restaurant_entities.models import Table
from django.core.exceptions import ValidationError
from .base import BaseForm


class TableForm(BaseForm):
    class Meta:
        model = Table
        fields = [
            'name',
            'code'
        ]

