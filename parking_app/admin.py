# from django.contrib import admin
# from .models import ParkingLot, Car

# class ParkingLotAdmin(admin.ModelAdmin):
#     list_display = ('square_footage', 'available_spots')
#     search_fields = ['square_footage']

# admin.site.register(ParkingLot, ParkingLotAdmin)

# class CarAdmin(admin.ModelAdmin):
#     list_display = ('license_plate',)
#     search_fields = ['license_plate']

# admin.site.register(Car, CarAdmin)

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