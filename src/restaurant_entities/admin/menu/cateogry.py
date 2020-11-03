from django.contrib import admin
from django.contrib.admin import ModelAdmin

from restaurant_entities.models import Category, CategoryTranslation


class CategoryTranslationInline(admin.TabularInline):
    model = CategoryTranslation

class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        CategoryTranslationInline,
    ]

admin.site.register(Category, CategoryAdmin)