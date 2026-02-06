from django.urls import path
from .views import VehicleListView, CreateVehicleView

urlpatterns = [
    path('create/', CreateVehicleView.as_view(), name='create-vehicle'),
    path('', VehicleListView.as_view(), name= 'vehicle-list')
]
