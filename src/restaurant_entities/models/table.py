from django.db import models
from .base import GlobalID


class Table(GlobalID, models.Model):
    table_code = models.CharField(max_length=100)

    def __str__(self):
        return self.table_code
