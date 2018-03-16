from rest_framework import viewsets, mixins
from rest_framework.decorators import list_route

from account.models import UserDetail
from api.models import Location, GeoFencing
from api.serializers import LocationSerializer, GeoFenceSerializer, UserSerializer


class GeoFenceViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = GeoFencing.objects.all()
    serializer_class = GeoFenceSerializer


class LocationViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = UserDetail.objects.all()
    serializer_class = UserSerializer


class UserAuthView(viewsets.GenericViewSet):

    def post(self, request):
        pass

