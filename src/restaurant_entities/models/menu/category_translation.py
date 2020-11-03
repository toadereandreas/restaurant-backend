from django.db import models
from ..base import GlobalID
from .category import Category
from .language import Language

class CategoryTranslation(GlobalID, models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)


    def __str__(self):
        return self.name