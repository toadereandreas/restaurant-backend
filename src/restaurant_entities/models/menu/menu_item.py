from django.db import models
from ..base import GlobalID
from .allergen import Allergen


class MenuItem(GlobalID, models.Model):
    picture = models.ImageField(upload_to="images")
    price = models.DecimalField(max_digits=5, decimal_places=2)
    allergens = models.ManyToManyField(Allergen, related_name="menu_item_allergens")

    def __str__(self):
        return str(self.price)
