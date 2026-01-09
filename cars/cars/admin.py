from django.contrib import admin
from cars.models import Car
from cars.models import Brand

# Register your models here.
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'price', 'factory_year', 'model_year')
    search_fields = ('model', 'brand')

admin.site.register(Brand, BrandAdmin)
admin.site.register(Car, CarAdmin)