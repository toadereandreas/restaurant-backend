from restaurant_entities.models import Booking
from django.core.exceptions import ValidationError
from .base import BaseForm


class BookingForm(BaseForm):
    class Meta:
        model = Booking
        fields = [
            'date_time',
            'table',
            'number_of_persons',
            'phone_number'
        ]
