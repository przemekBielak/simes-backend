from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import viewsets

from server.models import Sensor1, Sensor2, Data
from server.serializers import Sensor1Serializer, Sensor2Serializer, UserSerializer, DataSerializer


class Sensor1ViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Sensor1.objects.all()
    serializer_class = Sensor1Serializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class Sensor2ViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Sensor2.objects.all()
    serializer_class = Sensor2Serializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class DataViewSet(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]