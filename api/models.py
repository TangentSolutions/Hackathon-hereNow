from django.contrib.auth.models import User
from django.db import models
from account.models import UserDetail


class GeoFencing(models.Model):
    lon = models.FloatField()
    lat = models.FloatField()
    radius = models.IntegerField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="geo_fencing_user")


class Location(models.Model):
    def __unicode__(self):
        return "({0}, {1})".format(self.lat, self.long)
    
    long = models.FloatField()
    lat = models.FloatField()
    time = models.DateTimeField()
    is_safe = models.NullBooleanField (null=True, blank=True, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="location_user")

