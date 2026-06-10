from django.http import HttpRequest
from django.shortcuts import render
from django.http import HttpResponse


"""
view
"""

def mytest(request):
    return HttpResponse('hallo')