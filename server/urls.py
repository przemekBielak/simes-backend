from django.urls import path, include
from rest_framework.routers import DefaultRouter
from server import views

router = DefaultRouter()
router.register(r'sensors', views.SensorViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]