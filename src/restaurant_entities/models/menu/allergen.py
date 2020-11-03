from django.db import models
from ..base import GlobalID


class Allergen(GlobalID, models.Model):
    internal_name = models.CharField(max_length=100, default="")
    number = models.PositiveIntegerField(unique=True)

    def __str__(self):
        return str(self.number) + ". " + self.internal_name
