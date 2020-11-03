from django.contrib import admin
from django.contrib.admin import ModelAdmin

from restaurant_entities.models import Language

admin.site.register(Language)