import random
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Car, ParkingLot
from .serializers import CarSerializer, ParkingLotSerializer


class CarListView(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class ParkingLotDetailView(generics.RetrieveAPIView):
    queryset = ParkingLot.objects.all()
    serializer_class = ParkingLotSerializer
    lookup_field = 'pk'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class InitializeParkingLotView(APIView):
    def post(self, request, *args, **kwargs):
        square_footage = request.data.get('square_footage')
        spot_size_width = request.data.get('spot_size_width', 8)
        spot_size_length = request.data.get('spot_size_length', 12)

        parking_lot = ParkingLot.objects.create(
            square_footage=square_footage,
            spot_size_width=spot_size_width,
            spot_size_length=spot_size_length
        )
        parking_lot.initialize_parking_lot()
        return Response({'message': 'Parking lot initialized successfully.'})


class ParkCarView(generics.CreateAPIView):
    serializer_class = CarSerializer

    def perform_create(self, serializer):
        car = serializer.save()
        parking_lot = ParkingLot.objects.first()

        if parking_lot:
            size = len(parking_lot.parking_lot)
            spot_found = False

            for spot in range(size):
                try:
                    if parking_lot.park_vehicle(car, spot):
                        spot_found = True
                        return Response({'message': f"Car with license plate {car.license_plate} parked successfully in spot {spot}"})
                except ValueError as e:
                    print(f"Error: {e}")

            if not spot_found:
                return Response({'message': f"No available spots for car with license plate {car.license_plate}. Parking lot is full."})
        else:
            return Response({'message': 'Please initialize the parking lot first.'})
