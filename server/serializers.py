from rest_framework import serializers
from django.contrib.auth.models import User

from server.models import AcDcSensor, DcSensor1, DcSensor2Pv, DcSensor3LiIon, DcSensor4Scap, DcSensor5Charger, Data


class BaseSensorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        abstract = True
        read_only_fields = ['time']


class AcDcSensorSerializer(BaseSensorSerializer):
    class Meta(BaseSensorSerializer.Meta):
        model = AcDcSensor
        fields = ['url', 'id', 'voltage1Rms', 'voltage2Rms',
                  'voltage3Rms', 'current1Rms', 'current2Rms',
                  'current3Rms', 'pPower', 'qPower',
                  'sPower', 'pEnergy', 'qEnergy',
                  'currentThd', 'voltageThd', 'powerCos',
                  'frequence', 'status', 'time']


class DcSensor1Serializer(BaseSensorSerializer):
    class Meta(BaseSensorSerializer.Meta):
        model = DcSensor1
        fields = ['url', 'id', 'voltageCh1', 'currentCh1',
                  'powerDcCh1', 'energyDcCh1', 'statusCh1',
                  'temperatureCh1', 'voltageCh2', 'currentCh2',
                  'powerDcCh2', 'energyDcCh2', 'statusCh2',
                  'temperatureCh2', 'time']


class DcSensor2PvSerializer(BaseSensorSerializer):
    class Meta(BaseSensorSerializer.Meta):
        model = DcSensor2Pv
        fields = ['url', 'id', 'voltageCh1', 'currentCh1',
                  'powerDcCh1', 'energyDcCh1', 'statusCh1',
                  'temperatureCh1', 'voltageCh2', 'currentCh2',
                  'powerDcCh2', 'energyDcCh2', 'statusCh2',
                  'temperatureCh2', 'lighting', 'time']


class DcSensor3LiIonSerializer(BaseSensorSerializer):
    class Meta(BaseSensorSerializer.Meta):
        model = DcSensor3LiIon
        fields = ['url', 'id', 'voltageCh1', 'currentCh1',
                  'powerDcCh1', 'energyDcCh1', 'statusCh1',
                  'temperatureCh1', 'charge', 'cycles', 'voltageCh2', 'currentCh2',
                  'powerDcCh2', 'energyDcCh2', 'statusSoh',
                  'temperatureCh2', 'soc', 'capacity', 'time']


class DcSensor4ScapSerializer(BaseSensorSerializer):
    class Meta(BaseSensorSerializer.Meta):
        model = DcSensor4Scap
        fields = ['url', 'id', 'voltageCh1', 'currentCh1',
                  'powerDcCh1', 'energyDcCh1', 'statusCh1',
                  'temperatureCh1', 'charge', 'cycles', 'voltageCh2', 'currentCh2',
                  'powerDcCh2', 'energyDcCh2', 'statusSoh',
                  'temperatureCh2', 'soc', 'capacity', 'time']


class DcSensor5ChargerSerializer(BaseSensorSerializer):
    class Meta(BaseSensorSerializer.Meta):
        model = DcSensor5Charger
        fields = ['url', 'id', 'voltageCh1', 'currentCh1',
                  'powerDcCh1', 'energyDcCh1', 'statusCh1',
                  'temperatureCh1', 'charge', 'voltageCh2', 'currentCh2',
                  'powerDcCh2', 'energyDcCh2', 'status',
                  'temperatureCh2', 'soc', 'capacity', 'time']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'id', 'email', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class DataSerializer(serializers.HyperlinkedModelSerializer):
    acdc_sensor = AcDcSensorSerializer()
    dc_sensor1 = DcSensor1Serializer()
    dc_sensor2pv = DcSensor2PvSerializer()
    dc_sensor3liion = DcSensor3LiIonSerializer()
    dc_sensor4scap = DcSensor4ScapSerializer()
    dc_sensor5charger = DcSensor5ChargerSerializer()

    class Meta:
        model = Data
        fields = ['url', 'id', 'acdc_sensor', 'dc_sensor1', 'dc_sensor2pv',
                  'dc_sensor3liion', 'dc_sensor4scap', 'dc_sensor5charger']

    def create(self, validated_data):
        acdc_sensor_data = validated_data.pop('acdc_sensor')
        dc_sensor1_data = validated_data.pop('dc_sensor1')
        dc_sensor2pv_data = validated_data.pop('dc_sensor2pv')
        dc_sensor3liion_data = validated_data.pop('dc_sensor3liion')
        dc_sensor4scap_data = validated_data.pop('dc_sensor4scap')
        dc_sensor5charger_data = validated_data.pop('dc_sensor5charger')

        created_acdc_sensor = AcDcSensor.objects.create(**acdc_sensor_data)
        created_dc_sensor1 = DcSensor1.objects.create(**dc_sensor1_data)
        created_dc_sensor2pv = DcSensor2Pv.objects.create(**dc_sensor2pv_data)
        created_dc_sensor3liion = DcSensor3LiIon.objects.create(
            **dc_sensor3liion_data)
        created_dc_sensor4scap = DcSensor4Scap.objects.create(
            **dc_sensor4scap_data)
        created_dc_sensor5charger = DcSensor5Charger.objects.create(
            **dc_sensor5charger_data)

        data = Data.objects.create(
            acdc_sensor=created_acdc_sensor, dc_sensor1=created_dc_sensor1, dc_sensor2pv=created_dc_sensor2pv,
            dc_sensor3liion=created_dc_sensor3liion, dc_sensor4scap=created_dc_sensor4scap, dc_sensor5charger=created_dc_sensor5charger, **validated_data)

        return data
