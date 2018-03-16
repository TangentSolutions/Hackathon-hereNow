from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


class GeofenceViewSet(View):

    def post(self, request):
        return HttpResponse(request)
