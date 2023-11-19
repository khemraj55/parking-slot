from django.contrib import admin
from .models import Car, ParkingLot

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('license_plate',)

@admin.register(ParkingLot)
class ParkingLotAdmin(admin.ModelAdmin):
    list_display = ('id', 'square_footage', 'spot_size_width', 'spot_size_length')

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        obj.initialize_parking_lot()  # Initialize parking lot after saving in the admin interface