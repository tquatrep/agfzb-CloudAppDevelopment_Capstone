from django.contrib import admin
from .models import CarMake, CarModel


# Register your models here.

# CarModelInline class
class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 1

# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    fields = ['car_make', 'name', 'dealer_id', 'car_type', 'year']
    #inlines = [CarModelInline]

# CarMakeInline class
class CarMakeInline(admin.StackedInline):
    model = CarMake
    extra = 1

# CarMakeAdmin class
class CarMakeAdmin(admin.ModelAdmin):
    fields = ['name', 'description']
    #inlines = [CarMakeInline]

# Register models here
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)