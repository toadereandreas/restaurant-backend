from django.db import models
from .base import GlobalID


class Dummy(GlobalID, models.Model):
    test_name = models.CharField(max_length=100)
    test_age = models.PositiveIntegerField()
    test_agss = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.test_name


class Dummysss(GlobalID, models.Model):
    test_name = models.CharField(max_length=100)
    test_age = models.PositiveIntegerField()
    test_agss = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.test_name