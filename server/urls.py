from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from server import views

router = DefaultRouter()
router.register(r'acdc_sensor', views.AcDcSensorViewSet)
router.register(r'dc_sensor1', views.DcSensor1ViewSet)
router.register(r'dc_sensor2pv', views.DcSensor2PvViewSet)
router.register(r'dc_sensor3liion', views.DcSensor3LiIonViewSet)
router.register(r'dc_sensor4scap', views.DcSensor4ScapViewSet)
router.register(r'dc_sensor5charger', views.DcSensor5ChargerViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'data', views.DataViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('token', obtain_auth_token, name="auth_token")
]
