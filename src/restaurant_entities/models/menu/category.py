from django.db import models
from ..base import GlobalID


class Category(GlobalID, models.Model):
    internal_name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.internal_name