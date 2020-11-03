from django.db import models
from ..base import GlobalID
from .category import Category

class CategoryTranslation(GlobalID, models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name