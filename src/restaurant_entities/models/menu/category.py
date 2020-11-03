from django.db import models
from ..base import GlobalID


class Category(GlobalID, models.Model):
    pass

    def __str__(self):
        return "category"