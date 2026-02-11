from rest_framework import serializers
from .models import Vehicles, VehicleImages

class VehicleSerializer(serializers.ModelSerializer):
    images = serializers.ListField(
        child=serializers.ImageField(), write_only=True
    )
    
    class Meta:
        model = Vehicles
        fields = [
            'id', 'make', 'model', 'body_type', 'year', 'cost', 
            'engine', 'transmission', 'seats', 'gas_type', 'images'
        ]
    
    def create(self, validated_data):
        images = validated_data.pop('images', [])
        vehicle = Vehicles.objects.create(**validated_data)
        
        for image in images:
            VehicleImages.objects.create(
                vehicle_id = vehicle,
                image = image
            )
        return vehicle