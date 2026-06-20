from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets

from mytest.models import Music
from mytest.serializers import MusicSerializer
"""
view
"""

def mytest(request):
    return HttpResponse('hallo')
def login(request):
    return render(request, 'login.html')

# Create your views here.
def hello(request):
    return render(request, 'hello_django.html', {
        'data': "Hello Django ",
    })

# Create your views here.
class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer