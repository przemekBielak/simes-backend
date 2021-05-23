from django.db import models


class Sensor(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    voltage = models.IntegerField()
    current = models.IntegerField()

    class Meta:
        ordering = ['created']
