from django.db import models
from ..base import GlobalID
from .allergen import Allergen


class AllergenTranslation(GlobalID, models.Model):
    name = models.CharField(max_length=255)
    allergen = models.ForeignKey(Allergen, on_delete=models.CASCADE)

    def __str__(self):
        return self.name