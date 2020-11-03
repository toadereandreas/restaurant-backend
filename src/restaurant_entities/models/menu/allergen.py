from django.db import models
from ..base import GlobalID


class Allergen(GlobalID, models.Model):
    number = models.PositiveIntegerField()

    def __str__(self):
        return self.number