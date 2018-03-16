from django.conf.urls import url, include
from api.views import UserViewSet
from django.contrib import admin
from django.urls import path

from api import router


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', UserViewSet),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'api/', include(router))
]
