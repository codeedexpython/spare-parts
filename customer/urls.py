
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AddressViewSet

router = DefaultRouter()

router.register("addresses", AddressViewSet)

urlpatterns = [
    path('', include(router.urls)),
]