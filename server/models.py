from datetime import datetime

from django.db import models


class Sensor(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    voltage = models.FloatField()
    current = models.FloatField()
    owner = models.ForeignKey('auth.User', related_name='sensor_data', on_delete=models.CASCADE)
    time = models.DateTimeField()

    def save(self, *args, **kwargs):
        if self.time is None:
            self.time = datetime.now()
        super(Sensor, self).save(*args, **kwargs)

    class Meta:
        ordering = ['created']
