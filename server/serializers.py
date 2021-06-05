from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.relations import PrimaryKeyRelatedField

from server.models import Sensor1, Sensor2, Data


class Sensor1Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sensor1
        fields = ['url', 'id', 'voltage', 'current', 'power', 'energy', 'charge_cycles', 'temperature', 'status',
                  'error', 'time']
        read_only_fields = ['time']


class Sensor2Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sensor2
        fields = ['url', 'id', 'voltage', 'current', 'power', 'energy', 'charge_cycles', 'temperature', 'status',
                  'error', 'time']
        read_only_fields = ['time']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'id', 'username']


class DataSerializer(serializers.HyperlinkedModelSerializer):
    sensor1 = Sensor1Serializer()
    sensor2 = Sensor2Serializer()

    class Meta:
        model = Data
        fields = ['url', 'id', 'sensor1', 'sensor2']

    def create(self, validated_data):
        sensor1_data = validated_data.pop('sensor1')
        sensor2_data = validated_data.pop('sensor2')

        created1 = Sensor1.objects.create(**sensor1_data)
        created2 = Sensor2.objects.create(**sensor2_data)

        data = Data.objects.create(sensor1=created1, sensor2=created2, **validated_data)

        return data
