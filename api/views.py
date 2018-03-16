from rest_framework import viewsets, mixins
from api.models import GeoFencing
from api.serializers import GeoFenceSerializer

class GeofenceViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = GeoFencing.objects.all()
    serializer_class = GeoFenceSerializer
