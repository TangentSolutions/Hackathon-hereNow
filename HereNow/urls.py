from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from api.views import GeofenceViewSet

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^geofence/', GeofenceViewSet),
    url(r'^api-auth/', include('rest_framework.urls'))
]
