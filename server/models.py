from datetime import datetime

from django.db import models


class BaseSensor(models.Model):
    voltage = models.FloatField()
    current = models.FloatField()
    power = models.FloatField()
    temperature = models.FloatField()
    energy = models.FloatField()
    charge = models.FloatField()
    time = models.DateTimeField()

    class Meta:
        abstract = True


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


class Sensor3(BaseSensor):
    def save(self, *args, **kwargs):
        if self.time is None:
            self.time = datetime.now()
        super(Sensor3, self).save(*args, **kwargs)


class Sensor4(BaseSensor):
    def save(self, *args, **kwargs):
        if self.time is None:
            self.time = datetime.now()
        super(Sensor4, self).save(*args, **kwargs)


class Data(models.Model):
    sensor1 = models.OneToOneField(
        Sensor1, related_name='sensor1_data', on_delete=models.CASCADE)
    sensor2 = models.OneToOneField(
        Sensor2, related_name='sensor2_data', on_delete=models.CASCADE)
    sensor3 = models.OneToOneField(
        Sensor3, related_name='sensor3_data', on_delete=models.CASCADE)
    sensor4 = models.OneToOneField(
        Sensor4, related_name='sensor4_data', on_delete=models.CASCADE)
