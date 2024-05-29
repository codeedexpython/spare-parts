from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BrandViewSet, VehicleViewSet

router = DefaultRouter()
router.register("vehicle", VehicleViewSet)
router.register("brand", BrandViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
