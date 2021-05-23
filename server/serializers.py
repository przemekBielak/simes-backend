from rest_framework import serializers
from django.contrib.auth.models import User

from server.models import Sensor


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        owner = serializers.ReadOnlyField(source='owner.username')
        fields = ['id', 'voltage', 'current', 'owner', 'time']
        read_only_fields = ['time']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        sensor_data = serializers.PrimaryKeyRelatedField(many=True, queryset=Sensor.objects.all())
        fields = ['id', 'username', 'sensor_data']
