from rest_framework import serializers
from api.models import GeoFencing, User, Location

class GeoFenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeoFencing
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = '__all__'

        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'name', 'email', 'address', 'phone', 'related_users', 'created', 'role')

