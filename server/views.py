from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import viewsets

from server.models import Sensor1, Sensor2, Sensor3, Sensor4, Data
from server.serializers import Sensor1Serializer, Sensor2Serializer, Sensor3Serializer, Sensor4Serializer, UserSerializer, DataSerializer


class Sensor1ViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Sensor1.objects.all()
    serializer_class = Sensor1Serializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class Sensor2ViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Sensor2.objects.all()
    serializer_class = Sensor2Serializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class Sensor3ViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Sensor3.objects.all()
    serializer_class = Sensor3Serializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class Sensor4ViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Sensor4.objects.all()
    serializer_class = Sensor4Serializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Returns a list of all active users.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class DataViewSet(viewsets.ModelViewSet):
    """
    Returns data from all sensors.
    """
    queryset = Data.objects.all()
    serializer_class = DataSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
