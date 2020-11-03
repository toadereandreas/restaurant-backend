from django.db import models
from ..base import GlobalID


class Category(GlobalID, models.Model):
    internal_name = models.CharField(max_length=255)

    def __str__(self):
        return self.internal_name