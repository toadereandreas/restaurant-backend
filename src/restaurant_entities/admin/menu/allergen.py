from django.contrib import admin
from django.contrib.admin import ModelAdmin

from restaurant_entities.models import Allergen, AllergenTranslation


class AllergenTranslationInline(admin.TabularInline):
    model = AllergenTranslation

class AllergenAdmin(admin.ModelAdmin):
    inlines = [
        AllergenTranslationInline,
    ]

admin.site.register(Allergen, AllergenAdmin)
