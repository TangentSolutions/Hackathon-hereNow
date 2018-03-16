from django.db import models

class User(models.Model):
    def __unicode__(self):
        return self.username
    
    username = models.CharField(max_length=255, unique=True, db_index=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    address = models.TextField(null=True, blank=True, default=None)
    phone = models.TextField(null=True, blank=True, default=None)
    password = models.TextField(max_length=255)
    related_users = models.ForeignKey('User', on_delete=models.CASCADE, related_name="user_related_users", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    role = models.CharField(max_length=255)
    token = models.CharField(max_length=255, null=True, blank=True, default=None)
    last_modified = models.DateTimeField(auto_now=True)


class GeoFencing(models.Model):
    def __unicode__(self):
        return self.username
    
    lon = models.FloatField()
    lat = models.FloatField()
    radius = models.IntegerField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name="geo_fencing_user")


class Location(models.Model):
    def __unicode__(self):
        return "({0}, {1})".format(self.lat, self.lon)
    
    long = models.FloatField()
    lat = models.FloatField()
    time = models.DateTimeField()
    is_safe = models.NullBooleanField (null=True, blank=True, default=None)
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name="location_user")

