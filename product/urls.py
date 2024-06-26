from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register("categorie", CategoryViewSet)
router.register("review", ReviewViewSet)
router.register("year", YearViewset)

urlpatterns = [
    path('', include(router.urls)),
]