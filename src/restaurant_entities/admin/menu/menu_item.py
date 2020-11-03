from django.contrib import admin
from django.contrib.admin import ModelAdmin

from restaurant_entities.models import MenuItem, MenuItemTranslation


class MenuItemTranslationInline(admin.TabularInline):
    model = MenuItemTranslation

class MenuItemAdmin(admin.ModelAdmin):
    inlines = [
        MenuItemTranslationInline,
    ]

admin.site.register(MenuItem, MenuItemAdmin)
