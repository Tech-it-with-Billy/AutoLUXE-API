from django.shortcuts import render
from rest_framework import generics
from .serializers import BookingSerializer
from .models import Bookings

class CreateBookingView(generics.CreateAPIView):
    queryset = Bookings.objects.all()
    serializer_class = BookingSerializer

class BookingListView(generics.ListAPIView):
    queryset = Bookings.objects.all()
    serializer_class = BookingSerializer
