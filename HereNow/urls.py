from django.contrib import admin
from django.urls import path
from api.views import GeofenceViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('geofence/', GeofenceViewSet),
]
