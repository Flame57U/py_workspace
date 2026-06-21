from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.decorators import permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from mytest.models import Music, Share
from mytest.serializers import MusicSerializer, ShareSerializer
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
    permission_classes = (IsAuthenticated,)

class ShareViewSet(viewsets.ModelViewSet):
    queryset = Share.objects.all()
    serializer_class = ShareSerializer
    parser_classes = (JSONParser,)

    def get_permissions(self):
        if self.action in ('create',):
            self.permission_classes = [IsAuthenticated]
        return [permission() for permission in self.permission_classes]

    # [GET] api/shares/
    def list(self, request, **kwargs):
        shares = Share.objects.all()
        serializer = ShareSerializer(shares, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # [POST] api/shares/
    @permission_classes((IsAuthenticated,))
    def create(self, request, **kwargs):
        name = request.data.get('name')
        share = Share.objects.create(name=name)
        serializer = ShareSerializer(share)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

