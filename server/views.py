from rest_framework import generics

from server.models import Sensor
from server.serializers import SensorSerializer


class SensorList(generics.ListCreateAPIView):
    """
    List all sensor data, or create a new sensor.
    """
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a sensor data.
    """
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
