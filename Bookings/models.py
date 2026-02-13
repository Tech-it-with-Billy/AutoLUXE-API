from django.db import models
import uuid
from VehicleListing.models import Vehicles

# Create your models here.
class Bookings(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    vehicle_id = models.ForeignKey(Vehicles, on_delete=models.CASCADE, related_name='bookings')
    customer_name = models.CharField(max_length=50)
    customer_email = models.EmailField(unique=True)
    start_date = models.DateField()
    return_date = models.DateField()
    pick_up = models.CharField(max_length=50)
    drop_off = models.CharField(max_length=50)
    days = models.PositiveIntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Booking {self.id} - {self.customer_name}"
    
    def save(self, *args, **kwargs):
        if self.start_date and self.return_date:
            self.days = (self.return_date - self.start_date).days
        super().save(*args, **kwargs)