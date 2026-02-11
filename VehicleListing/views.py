from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Vehicles
from .serializers import VehicleSerializer, VehicleCreateSerializer

class CreateVehicleView(generics.CreateAPIView):
    queryset = Vehicles.objects.all()
    serializer_class = VehicleCreateSerializer
    parser_classes = [MultiPartParser, FormParser]

class VehicleListView(generics.ListAPIView):
    queryset = Vehicles.objects.all()
    serializer_class = VehicleSerializer
