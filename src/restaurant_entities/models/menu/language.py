from django.db import models
from ..base import GlobalID


class Language(GlobalID, models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=3)

    def __str__(self):
        return self.name
