from rest_framework import generics
from rest_framework import mixins

from server.models import Sensor
from server.serializers import SensorSerializer


class SensorList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    """
    List all sensor data, or create a new sensor.
    """
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class SensorDetails(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    """
    Retrieve, update or delete a sensor data.
    """
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
