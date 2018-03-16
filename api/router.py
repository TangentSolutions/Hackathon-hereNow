from django.conf.urls import url, include
from rest_framework import routers

from api.views import LocationViewSet

router = routers.SimpleRouter()

router.register(r'locations', LocationViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]
