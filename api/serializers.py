from rest_framework import serializers

from account.models import UserDetail
from api.models import Location


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetail
        exclude = ('date_added', )


