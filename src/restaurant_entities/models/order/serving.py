from django.db import models
from ..base import GlobalID
from ...users.models import CustomUser


class Serving(GlobalID, models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=4, unique=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE) 
    # called = models.BooleanField() 
