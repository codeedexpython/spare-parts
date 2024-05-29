from rest_framework import serializers
from.models import Brand, Vehicle

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name', 'image']

class VehicleSerializer(serializers.ModelSerializer):
    brand_id = serializers.PrimaryKeyRelatedField(queryset=Brand.objects.all(), source='brand', write_only=True)
    brand = BrandSerializer(read_only=True)

    class Meta:
        model = Vehicle
        fields = ['id', 'name', 'image', 'brand_id', 'brand']

    