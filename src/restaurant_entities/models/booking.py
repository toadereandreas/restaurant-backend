from django.db import models
from .base import GlobalID
from .table import Table


class Booking(GlobalID, models.Model):
    date_time = models.DateTimeField()
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    number_of_persons = models.PositiveIntegerField()
    phone_number = models.CharField(max_length=50)

    def __str__(self):
        return self.table.name + " no.persons: " + str(self.number_of_persons) + " contact: " + self.phone_number
