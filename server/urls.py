from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from server import views

urlpatterns = [
    path('', views.api_root),
    path('sensors/', views.SensorList.as_view(), name='sensor-list'),
    path('sensors/<int:pk>/', views.SensorDetails.as_view(), name='sensor-detail'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)
