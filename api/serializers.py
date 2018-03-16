from rest_framework import serializers
from api.models import GeoFencing

class GeoFenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeoFencing
        fields = '__all__'