from rest_framework import serializers
from .models import Category,Product,Review,ModelYear

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'image', 'name']



class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class YearSerializers(serializers.ModelSerializer):
    class Meta:
        model = ModelYear
        fields = '__all__'