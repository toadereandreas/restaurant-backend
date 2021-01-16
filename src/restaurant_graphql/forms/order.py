from restaurant_entities.models.order import Order
from restaurant_entities.models.order import Serving
from django.core.exceptions import ValidationError
from .base import BaseForm
from django import forms


class OrderForm(BaseForm):
    class Meta:
        model = Order
        fields = [
            'serving',
            'color',
            'note',
            'locked',
        ]

    serving = forms.UUIDField(required=True)

    def clean_serving(self):
        gid = self.cleaned_data.get('serving')
        serving = Serving.objects.get(gid=gid)
        if not serving:
            raise ValidationError(
                "Serving does not exist."
            )
        return serving

    def clean(self):
        super().clean()
