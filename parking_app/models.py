import json
from django.db import models
import boto3


class Car(models.Model):
    license_plate = models.CharField(max_length=7, unique=True)

    def __str__(self):
        return f"Car with license plate {self.license_plate}"


class ParkingLot(models.Model):
    square_footage = models.IntegerField()
    spot_size_width = models.IntegerField(default=8)
    spot_size_length = models.IntegerField(default=12)
    parking_lot = models.JSONField(default=list)

    def calculate_parking_lot_size(self):
        spot_area = self.spot_size_width * self.spot_size_length
        return self.square_footage // spot_area

    def initialize_parking_lot(self):
        size = self.calculate_parking_lot_size()
        self.parking_lot = [None] * size
        self.save(update_fields=['parking_lot'])

    def car_to_dict(self, car):
        return {'license_plate': car.license_plate}

    def park_vehicle(self, car, spot):
        if not (0 <= spot < len(self.parking_lot)):
            raise ValueError("Invalid spot number")

        if self.parking_lot[spot] is None:
            car_dict = self.car_to_dict(car)
            self.parking_lot[spot] = car_dict
            self.save(update_fields=['parking_lot'])
            return True
        else:
            return False

    def map_vehicles_to_spots(self):
        mapping = {}

        for i, car_data in enumerate(self.parking_lot):
            if car_data:
                mapping[car_data['license_plate']] = i

        return mapping

    def save_mapping_to_s3(self, filename, bucket_name):
        mapping = self.map_vehicles_to_spots()
        with open(filename, 'w') as file:
            json.dump(mapping, file)

        s3 = boto3.client('s3')
        s3.upload_file(filename, bucket_name, filename)
