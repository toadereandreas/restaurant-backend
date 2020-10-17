from windshopper_entities.models import Dummy
from django.core.exceptions import ValidationError
from .base import BaseForm


class DummyForm(BaseForm):
    class Meta:
        model = Dummy
        fields = [
            'test_age',
            'test_name',
        ]

    def clean_test_age(self):
        if self.data['test_age'] > 150:
            raise ValidationError(
                "Oh ma gad!"
            )
        return self.data['test_age']
