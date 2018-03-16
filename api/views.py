from rest_framework import viewsets, mixins
from api.models import GeoFencing, User
from api.serializers import GeoFenceSerializer, UserSerializer

class GeofenceViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = GeoFencing.objects.all()
    serializer_class = GeoFenceSerializer


# Create your views here.
class UserViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
