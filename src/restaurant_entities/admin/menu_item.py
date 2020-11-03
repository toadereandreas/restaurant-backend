from django.contrib import admin
from django.contrib.admin import ModelAdmin

from restaurant_entities.models import MenuItem


admin.site.register(MenuItem)