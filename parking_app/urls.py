from django.urls import path
from .views import CarListView, ParkingLotDetailView, ParkCarView

urlpatterns = [
    path('cars/', CarListView.as_view(), name='car-list'),
    path('parking-lot/', ParkingLotDetailView.as_view(), name='parking-lot-detail'),
    path('parking-lot/<int:pk>/', ParkingLotDetailView.as_view(),
         name='parking-lot-detail'),
    path('park-car/', ParkCarView.as_view(), name='park-car'),
]
