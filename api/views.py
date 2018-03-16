from rest_framework import viewsets, mixins
from api.models import Location
from api.serializers import LocationSerializer


class LocationViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer