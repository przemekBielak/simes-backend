from django.db import models


class Sensor(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    voltage = models.FloatField()
    current = models.FloatField()
    owner = models.ForeignKey('auth.User', related_name='sensor_data', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']
