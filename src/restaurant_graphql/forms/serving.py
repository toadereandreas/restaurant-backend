from restaurant_entities.models.order import Serving
from django.core.exceptions import ValidationError
from .base import BaseForm


class ServingForm(BaseForm):
    class Meta:
        model = Serving
        fields = [
            'code',
            'user',
            'name'
        ]