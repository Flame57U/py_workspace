from django.urls import path
from . import views
urlpatterns = [
    path('', views.mytest, name = 'mytest'),
]
