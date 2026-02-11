from django.db import models
import uuid

class Vehicles(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    body_type = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    engine = models.IntegerField()
    transmission = models.CharField(max_length=50)
    seats = models.IntegerField()
    gas_type = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.make} {self.model} {self.year} - {self.cost}'
    
class VehicleImages(models.Model):
    vehicle_id = models.ForeignKey(Vehicles, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='vehicleImages/')
