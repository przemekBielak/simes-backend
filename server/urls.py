from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from server import views

urlpatterns = [
    path('sensor/', views.sensor_list),
    path('sensor/<int:pk>/', views.sensor_detail)
]

urlpatterns = format_suffix_patterns(urlpatterns)
