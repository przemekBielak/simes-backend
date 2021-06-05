from datetime import datetime

from django.db import models


class BaseSensor(models.Model):
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

    class Meta:
        abstract = True
        ordering = ['created']


class Sensor1(BaseSensor):
    def save(self, *args, **kwargs):
        if self.time is None:
            self.time = datetime.now()
        super(Sensor1, self).save(*args, **kwargs)


class Sensor2(BaseSensor):
    def save(self, *args, **kwargs):
        if self.time is None:
            self.time = datetime.now()
        super(Sensor2, self).save(*args, **kwargs)


class Data(models.Model):
    sensor1 = models.OneToOneField(Sensor1, related_name='sensor1_data', on_delete=models.CASCADE)
    sensor2 = models.OneToOneField(Sensor2, related_name='sensor2_data', on_delete=models.CASCADE)
