from rest_framework import serializers

from account.models import UserDetail
from api.models import Location


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()
    username = serializers.SerializerMethodField()
    role_type = serializers.SerializerMethodField()

    class Meta:
        model = UserDetail
        fields = ('id', 'username', 'first_name', 'last_name', 'role', 'role_type', 'related_users')

    @staticmethod
    def get_related_users():
        pass

    @staticmethod
    def get_username(user_detail):
        return '{}'.format(user_detail.user.username)

    @staticmethod
    def get_first_name(user_detail):
        return '{}'.format(user_detail.user.first_name)

    @staticmethod
    def get_last_name(user_detail):
        return '{}'.format(user_detail.user.last_name)

    @staticmethod
    def get_role_type(user_detail):
        if user_detail.role:
            return '{}'.format(user_detail.role.description)

        return None


