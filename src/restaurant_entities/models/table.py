from django.db import models
from .base import GlobalID


class Table(GlobalID, models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.IntegerField(unique=True)

    def __str__(self):
        return self.name + " - " + str(self.code)
