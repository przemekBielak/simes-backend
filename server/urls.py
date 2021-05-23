from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from server import views

urlpatterns = [
    path('', views.SensorList.as_view()),

    path('sensors/', views.SensorList.as_view()),
    path('sensors/<int:pk>/', views.SensorDetails.as_view()),

    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
