from django.db import models
from ..base import GlobalID
from .serving import Serving


class Order(GlobalID, models.Model):
    serving = models.ForeignKey(Serving, on_delete=models.CASCADE)
    color = models.CharField(max_length=50)
    note = models.TextField()
    locked = models.BooleanField(default=False)
