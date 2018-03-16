from django.conf.urls import url, include
from api.views import UserViewSet
from django.contrib import admin
from django.urls import path

from api import router
from api.views import UserAuthView


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'user/login/', UserAuthView.as_view()),
    url(r'api/', include(router))
]
