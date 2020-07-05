from django.contrib import admin
from django.urls import path
from rest_framework import routers
from backend import views

urlpatterns = [
    path(r'abc/', views.abc),
]

router = routers.DefaultRouter()
router.register(r'visitor', views.VisitorViewSet)
router.register(r'hotel', views.HotelViewSet)

urlpatterns += router.urls
