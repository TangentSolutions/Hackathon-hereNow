from django.conf.urls import url, include
from rest_framework import routers

from api.views import LocationViewSet, GeoFenceViewSet

router = routers.SimpleRouter()

router.register(r'locations', LocationViewSet)
router.register(r'geofence', GeoFenceViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]
