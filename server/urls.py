from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from server import views

urlpatterns = [
    path('sensor/', views.SensorList.as_view()),
    path('sensor/<int:pk>/', views.SensorDetails.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
