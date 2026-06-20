from django.urls import path,include
from . import views
from .models import Music
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'music', Music)
urlpatterns = [
    path('', views.mytest, name = 'mytest'),
    path('login/', views.login, name = 'login'),
    path('hallo/', views.hello, name='hello_view'),

    path('api/', include(router.urls)),
]
