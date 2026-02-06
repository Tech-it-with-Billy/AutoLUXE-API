from django.shortcuts import render
from .models import Vehicles
from .serializers import VehicleSerializer

from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser

# Create your views here.
class CreateVehicleView(generics.CreateAPIView):
    queryset = Vehicles.objects.all()
    serializer_class = VehicleSerializer
    parser_classes = [MultiPartParser, FormParser]

class VehicleListView(generics.ListAPIView):
    queryset = Vehicles.objects.all()
    serializer_class = VehicleSerializer
    