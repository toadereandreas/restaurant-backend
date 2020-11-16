from django.contrib import admin
from django.contrib.admin import ModelAdmin

from restaurant_entities.models import Booking, Table


class BookingInline(admin.TabularInline):
    model = Booking

class TableAdmin(admin.ModelAdmin):
    inlines = [
        BookingInline,
    ]

admin.site.register(Table, TableAdmin)
