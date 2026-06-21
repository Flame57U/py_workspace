from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'music', views.MusicViewSet)
router.register(r'shares', views.ShareViewSet)
urlpatterns = [
    path('', views.mytest, name = 'mytest'),
    path('login/', views.login, name = 'login'),
    path('hallo/', views.hello, name='hello_view'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include(router.urls)),
]
