from django.contrib import admin
from .models import Car


class CarAdmin(admin.ModelAdmin):
    fields = ['slot', 'color', 'r_no']
    search_fields = ['slot', 'color', 'r_no']

admin.site.register(Car, CarAdmin)
