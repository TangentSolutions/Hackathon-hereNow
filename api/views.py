from django.contrib.auth.models import User
from rest_framework import viewsets, mixins, permissions
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from account.models import UserDetail
from api.models import Location, GeoFencing
from api.serializers import LocationSerializer, GeoFenceSerializer, UserSerializer


class GeoFenceViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = GeoFencing.objects.all()
    serializer_class = GeoFenceSerializer


class LocationViewSet(mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.ListModelMixin,
                      viewsets.GenericViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    @detail_route(methods=['get'])
    def user(self, request, pk=None):
        locations = Location.objects.filter(user__id=pk)

        serializer = LocationSerializer(
            locations, many=True, context={'request': request})
        return Response(serializer.data)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = UserDetail.objects.all()
    serializer_class = UserSerializer


class UserAuthView(viewsets.GenericViewSet):

    def post(self, request):
        pass

