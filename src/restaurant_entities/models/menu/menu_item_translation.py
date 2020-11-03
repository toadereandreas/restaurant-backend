from django.db import models
from ..base import GlobalID
from .menu_item import MenuItem
from .allergen import Allergen
from .category import Category
from .language import Language


class MenuItemTranslation(GlobalID, models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
   
    def __str__(self):
        return self.name
