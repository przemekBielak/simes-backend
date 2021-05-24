from rest_framework import serializers
from django.contrib.auth.models import User

from server.models import Sensor


class SensorSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Sensor
        fields = ['url', 'id', 'voltage', 'current', 'time', 'owner']
        read_only_fields = ['time', 'owner']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    sensor_data = serializers.HyperlinkedRelatedField(many=True, view_name='sensor-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'sensor_data']
