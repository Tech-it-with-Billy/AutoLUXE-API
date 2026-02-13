from django.urls import path
from .views import CreateBookingView, BookingListView

urlpatterns = [
    path('create/', CreateBookingView.as_view(), name='create-bookings'),
    path('', BookingListView.as_view(), name='booking-list')
]
