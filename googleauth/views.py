from django.shortcuts import render
from django import views
from django.http import HttpResponse
from pydrive.auth import GoogleAuth

# Create your views here.

class GoogleAuthView(views.View):
    def get(self, request, *args, **kwargs):
        gauth = GoogleAuth()
        gauth.LocalWebserverAuth()
        return HttpResponse('GET request!')

    def post(self, request, *args, **kwargs):
        return HttpResponse('POST request!')
