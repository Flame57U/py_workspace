from django.shortcuts import render
from django.http import HttpResponse

"""
view
"""

def mytest(request):
    return HttpResponse('hallo')
def login(request):
    return render(request, 'login.html')
