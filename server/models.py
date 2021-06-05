from datetime import datetime

from django.db import models


class Sensor1(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    voltage = models.FloatField()
    current = models.FloatField()
    power = models.FloatField()
    energy = models.FloatField()
    charge_cycles = models.FloatField()
    temperature = models.FloatField()
    status = models.IntegerField()
    error = models.IntegerField()
    time = models.DateTimeField()

    def save(self, *args, **kwargs):
        if self.time is None:
            self.time = datetime.now()
        super(Sensor1, self).save(*args, **kwargs)

    class Meta:
        ordering = ['created']


class Sensor2(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    voltage = models.FloatField()
    current = models.FloatField()
    power = models.FloatField()
    energy = models.FloatField()
    charge_cycles = models.FloatField()
    temperature = models.FloatField()
    status = models.IntegerField()
    error = models.IntegerField()
    time = models.DateTimeField()

    def save(self, *args, **kwargs):
        if self.time is None:
            self.time = datetime.now()
        super(Sensor2, self).save(*args, **kwargs)

    class Meta:
        ordering = ['created']


class Data(models.Model):
    sensor1 = models.OneToOneField(Sensor1, related_name='sensor1_data', on_delete=models.CASCADE)
    sensor2 = models.OneToOneField(Sensor2, related_name='sensor2_data', on_delete=models.CASCADE)
