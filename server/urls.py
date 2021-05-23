from django.urls import path
from server import views

urlpatterns = [
    path('sensor/', views.sensor_list),
    path('sensor/<int:pk>/', views.sensor_detail)
]