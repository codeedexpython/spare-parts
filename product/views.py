from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from .models import Category,Product,Review,ModelYear
from .serializers import CategorySerializer,ProductSerializer,ReviewSerializer,YearSerializers
# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class YearViewset(viewsets.ModelViewSet):
    queryset = ModelYear.objects.all()
    serializer_class = YearSerializers