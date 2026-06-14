from django.urls import path
from . import views
urlpatterns = [
    path('', views.mytest, name = 'mytest'),
    path('login/', views.login, name = 'login'),
]
