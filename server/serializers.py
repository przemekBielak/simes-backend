from rest_framework import serializers
from django.contrib.auth.models import User

from server.models import Sensor1, Sensor2, Sensor3, Sensor4, Data


class BaseSensorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        abstract = True
        fields = ['url', 'id', 'voltage', 'current',
                  'power', 'temperature', 'energy', 'charge', 'time']
        read_only_fields = ['time']


class Sensor1Serializer(BaseSensorSerializer):
    class Meta(BaseSensorSerializer.Meta):
        model = Sensor1


class Sensor2Serializer(BaseSensorSerializer):
    class Meta(BaseSensorSerializer.Meta):
        model = Sensor2


class Sensor3Serializer(BaseSensorSerializer):
    class Meta(BaseSensorSerializer.Meta):
        model = Sensor3


class Sensor4Serializer(BaseSensorSerializer):
    class Meta(BaseSensorSerializer.Meta):
        model = Sensor4


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'id', 'username']


class DataSerializer(serializers.HyperlinkedModelSerializer):
    sensor1 = Sensor1Serializer()
    sensor2 = Sensor2Serializer()
    sensor3 = Sensor3Serializer()
    sensor4 = Sensor4Serializer()

    class Meta:
        model = Data
        fields = ['url', 'id', 'sensor1', 'sensor2', 'sensor3', 'sensor4']

    def create(self, validated_data):
        sensor1_data = validated_data.pop('sensor1')
        sensor2_data = validated_data.pop('sensor2')
        sensor3_data = validated_data.pop('sensor3')
        sensor4_data = validated_data.pop('sensor4')

        created1 = Sensor1.objects.create(**sensor1_data)
        created2 = Sensor2.objects.create(**sensor2_data)
        created3 = Sensor3.objects.create(**sensor3_data)
        created4 = Sensor4.objects.create(**sensor4_data)

        data = Data.objects.create(
            sensor1=created1, sensor2=created2, sensor3=created3, sensor4=created4, **validated_data)

        return data
