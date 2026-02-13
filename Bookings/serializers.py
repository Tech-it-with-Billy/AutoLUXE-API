from rest_framework import serializers
from .models import Bookings
from VehicleListing.models import Vehicles

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookings
        fieldsets = (
            "id", "vehicle_id", "customer_name", "customer_email", "start_date", 
            "return_date", "pick_up", "drop_off", "days", "total", "created_at"
        )
        read_only_fields = ("id", "days", "total", "created_at")
    
    def validate(self, data):
        start_date = data.get("start_date")
        return_date = data.get("return_date")
        
        if start_date >= return_date:
            raise serializers.ValidationError(
                "Return date must be after start date."
            )
        
        return data
    
    def create(self, validated_data):
        vehicle_id = validated_data.pop("vehicle_id")
        
        try:
            vehicle = Vehicles.objects.get(id=vehicle_id)
        except Vehicles.DoesNotExist:
            raise serializers.ValidationError(
                {"vehicle_id": "Vehicle not found."}
            )
        
        start_date = validated_data["start_date"]
        return_date = validated_data["return_date"]
        
        days = (return_date - start_date).days
        total = vehicle.price_per_day * days
        
        booking = Bookings.objects.create(
            vehicle = vehicle,
            days = days,
            total = total,
            **validated_data
        )
        
        return booking