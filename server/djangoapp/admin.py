from django.contrib import admin
from .models import CarMake, CarModel


# Register your models here.

# CarModelInline class
class CarModelInline(admin.TabularInline):  # or admin.StackedInline
    model = CarModel
    extra = 1  # how many empty forms to show


# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'car_make', )  # columns to show
    list_filter = ('car_make',)          # add filter by car_make
    search_fields = ('car_make__name',)  # allow searching by make name


# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]


# Register models here
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
