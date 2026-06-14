from django.http import HttpRequest
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

"""
view
"""

def mytest(request):
    return HttpResponse('hallo')
def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())