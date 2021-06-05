from django.urls import path, include
from rest_framework.routers import DefaultRouter
from server import views

router = DefaultRouter()
router.register(r'sensor1', views.Sensor1ViewSet)
router.register(r'sensor2', views.Sensor2ViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'data', views.DataViewSet)

urlpatterns = [
    path('', include(router.urls)),
]