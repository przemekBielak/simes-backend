from datetime import datetime

from django.db import models


class AcDcSensor:
    voltage1Rms = models.FloatField()
    voltage2Rms = models.FloatField()
    voltage3Rms = models.FloatField()
    current1Rms = models.FloatField()
    current2Rms = models.FloatField()
    current3Rms = models.FloatField()
    pPower = models.FloatField()
    qPower = models.FloatField()
    sPower = models.FloatField()
    pEnergy = models.FloatField()
    qEnergy = models.FloatField()
    currentThd = models.FloatField()
    voltageThd = models.FloatField()
    powerCos = models.FloatField()
    frequence = models.FloatField()
    status = models.IntegerField()

    def save(self, *args, **kwargs):
        if self.time is None:
            self.time = datetime.now()
        super(AcDcSensor, self).save(*args, **kwargs)


class DcSensor1:
    voltageCh1 = models.FloatField()
    currentCh1 = models.FloatField()
    powerDcCh1 = models.FloatField()
    energyDcCh1 = models.FloatField()
    statusCh1 = models.IntegerField()
    temperatureCh1 = models.FloatField()

    voltageCh2 = models.FloatField()
    currentCh2 = models.FloatField()
    powerDcCh2 = models.FloatField()
    energyDcCh2 = models.FloatField()
    statusCh2 = models.IntegerField()
    temperatureCh2 = models.FloatField()

    def save(self, *args, **kwargs):
        if self.time is None:
            self.time = datetime.now()
        super(DcSensor1, self).save(*args, **kwargs)


class DcSensor2Pv:
    voltageCh1 = models.FloatField()
    currentCh1 = models.FloatField()
    powerDcCh1 = models.FloatField()
    energyDcCh1 = models.FloatField()
    statusCh1 = models.IntegerField()
    temperatureCh1 = models.FloatField()

    voltageCh2 = models.FloatField()
    currentCh2 = models.FloatField()
    powerDcCh2 = models.FloatField()
    energyDcCh2 = models.FloatField()
    statusCh2 = models.IntegerField()
    temperatureCh2 = models.FloatField()
    lighting = models.FloatField()

    def save(self, *args, **kwargs):
        if self.time is None:
            self.time = datetime.now()
        super(DcSensor2Pv, self).save(*args, **kwargs)


class DcSensor3LiIon:
    voltageCh1 = models.FloatField()
    currentCh1 = models.FloatField()
    powerDcCh1 = models.FloatField()
    energyDcCh1 = models.FloatField()
    statusCh1 = models.IntegerField()
    temperatureCh1 = models.FloatField()
    charge = models.FloatField()
    cycles = models.IntegerField()

    voltageCh2 = models.FloatField()
    currentCh2 = models.FloatField()
    powerDcCh2 = models.FloatField()
    energyDcCh2 = models.FloatField()
    statusSoh = models.IntegerField()
    temperatureCh2 = models.FloatField()
    soc = models.FloatField()
    capacity = models.FloatField()

    def save(self, *args, **kwargs):
        if self.time is None:
            self.time = datetime.now()
        super(DcSensor3LiIon, self).save(*args, **kwargs)


class DcSensor4Scap:
    voltageCh1 = models.FloatField()
    currentCh1 = models.FloatField()
    powerDcCh1 = models.FloatField()
    energyDcCh1 = models.FloatField()
    statusCh1 = models.IntegerField()
    temperatureCh1 = models.FloatField()
    charge = models.FloatField()
    cycles = models.IntegerField()

    voltageCh2 = models.FloatField()
    currentCh2 = models.FloatField()
    powerDcCh2 = models.FloatField()
    energyDcCh2 = models.FloatField()
    statusSoh = models.IntegerField()
    temperatureCh2 = models.FloatField()
    soc = models.FloatField()
    capacity = models.FloatField()

    def save(self, *args, **kwargs):
        if self.time is None:
            self.time = datetime.now()
        super(DcSensor4Scap, self).save(*args, **kwargs)


class DcSensor5Charger:
    voltageCh1 = models.FloatField()
    currentCh1 = models.FloatField()
    powerDcCh1 = models.FloatField()
    energyDcCh1 = models.FloatField()
    statusCh1 = models.IntegerField()
    temperatureCh1 = models.FloatField()
    charge = models.FloatField()

    voltageCh2 = models.FloatField()
    currentCh2 = models.FloatField()
    powerDcCh2 = models.FloatField()
    energyDcCh2 = models.FloatField()
    status = models.IntegerField()
    temperatureCh2 = models.FloatField()
    soc = models.FloatField()
    capacity = models.FloatField()

    def save(self, *args, **kwargs):
        if self.time is None:
            self.time = datetime.now()
        super(DcSensor5Charger, self).save(*args, **kwargs)




class Data(models.Model):
    acdc_sensor = models.OneToOneField(
        AcDcSensor, related_name='acdc_sensor_data', on_delete=models.CASCADE)
    dc_sensor1 = models.OneToOneField(
        DcSensor1, related_name='dc_sensor1_data', on_delete=models.CASCADE)
    dc_sensor2pv = models.OneToOneField(
        DcSensor2Pv, related_name='dc_sensor2pv_data', on_delete=models.CASCADE)
    dc_sensor3liion = models.OneToOneField(
        DcSensor3LiIon, related_name='dc_sensor3liion_data', on_delete=models.CASCADE)
    dc_sensor4scap = models.OneToOneField(
        DcSensor4Scap, related_name='dc_sensor4scap_data', on_delete=models.CASCADE)
    dc_sensor5charger = models.OneToOneField(
        DcSensor5Charger, related_name='dc_sensor5charger_data', on_delete=models.CASCADE)
