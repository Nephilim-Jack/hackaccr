from django.db import models

# Create your models here.
class Point(models.Model):
    name = models.CharField(max_length=256)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)

    hasRestaurant = models.BooleanField(default=False)
    hasSleepPoint = models.BooleanField(default=False)
    isSecure = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    