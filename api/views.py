from rest_framework import viewsets, mixins
from api.models import Location, GeoFencing, User
from api.serializers import LocationSerializer, GeoFenceSerializer, UserSerializer

class GeoFenceViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = GeoFencing.objects.all()
    serializer_class = GeoFenceSerializer


class UserViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LocationViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
