from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from server.models import AcDcSensor, DcSensor1, DcSensor2Pv, DcSensor3LiIon, DcSensor4Scap, DcSensor5Charger, Data
from server.serializers import AcDcSensorSerializer, DcSensor1Serializer, DcSensor2PvSerializer, DcSensor3LiIonSerializer, DcSensor4ScapSerializer, DcSensor5ChargerSerializer, UserSerializer, DataSerializer


class AcDcSensorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AcDcSensor.objects.all()
    serializer_class = AcDcSensorSerializer
    permission_classes = (IsAuthenticated,)


class DcSensor1ViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DcSensor1.objects.all()
    serializer_class = DcSensor1Serializer
    permission_classes = (IsAuthenticated,)


class DcSensor2PvViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DcSensor2Pv.objects.all()
    serializer_class = DcSensor2PvSerializer
    permission_classes = (IsAuthenticated,)


class DcSensor3LiIonViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DcSensor3LiIon.objects.all()
    serializer_class = DcSensor3LiIonSerializer
    permission_classes = (IsAuthenticated,)


class DcSensor4ScapViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DcSensor4Scap.objects.all()
    serializer_class = DcSensor4ScapSerializer
    permission_classes = (IsAuthenticated,)


class DcSensor5ChargerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DcSensor5Charger.objects.all()
    serializer_class = DcSensor5ChargerSerializer
    permission_classes = (IsAuthenticated,)


class UserViewSet(viewsets.ModelViewSet):
    """
    Returns a list of all active users.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)


class DataViewSet(viewsets.ModelViewSet):
    """
    Returns data from all sensors.
    """
    queryset = Data.objects.all()
    serializer_class = DataSerializer
    permission_classes = (IsAuthenticated,)
