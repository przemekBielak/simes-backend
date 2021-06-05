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
    sensor2 = Sensor1Serializer()

    class Meta:
        model = Data
        fields = ['url', 'id', 'sensor1', 'sensor2']
    #
    # def create(self, validated_data):
    #     sensor1_data = validated_data.pop('sensor1')
    #     sensor2_data = validated_data.pop('sensor2')
    # 
    #     data = Data.objects.create(**validated_data)
    #
    #     Sensor1.objects.create()
    #
    #     # instance = Sensor1.objects.create(**validated_data['sensor1'])
    #     # instance2 = Sensor2.objects.create(**validated_data['sensor2'])
    #     print(validated_data)
    #     return Data(**validated_data)
