from django.conf.urls import url, include
from rest_framework import routers

from api.views import LocationViewSet, UserViewSet

router = routers.SimpleRouter()

router.register(r'locations', LocationViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]
