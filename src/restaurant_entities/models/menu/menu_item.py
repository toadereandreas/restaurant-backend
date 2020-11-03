from django.db import models
from ..base import GlobalID
from .allergen import Allergen
from .category import Category


class MenuItem(GlobalID, models.Model):
    internal_name = models.CharField(max_length=255)
    picture = models.ImageField(upload_to="images")
    price = models.DecimalField(max_digits=5, decimal_places=2)
    allergens = models.ManyToManyField(Allergen, related_name="menu_item_allergens", blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.internal_name
