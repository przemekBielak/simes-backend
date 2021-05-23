from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import permissions
from server.models import Sensor
from server.permissions import IsOwnerOrReadOnly
from server.serializers import SensorSerializer, UserSerializer


class SensorList(generics.ListCreateAPIView):
    """
    List all sensor data, or create a new sensor.
    """
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SensorDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a sensor data.
    """
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
