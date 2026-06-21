from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.decorators import permission_classes, action
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from mytest.models import fun_raw_sql_query, fun_sql_cursor_update
from django.shortcuts import get_object_or_404
from mytest.models import Music, Share
from mytest.serializers import MusicSerializer, MusicSerializerV1, ShareSerializer

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

    # /api/music/{pk}/detail/
    @action(detail=True, methods=['get'], url_path='detail')
    def get_detail(self, request, pk=None):
        music = get_object_or_404(Music, pk=pk)
        result = {
            'singer': music.singer,
            'song': music.song
        }

        return Response(result, status=status.HTTP_200_OK)

    # /api/music/all_singer/
    @action(detail=False, methods=['get'])
    def all_singer(self, request):
        music = Music.objects.values_list('singer', flat=True).distinct()
        return Response(music, status=status.HTTP_200_OK)

    # /api/music/raw_sql_query/
    @action(detail=False, methods=['get'])
    def raw_sql_query(self, request):
        song = request.query_params.get('song', None)
        music = fun_raw_sql_query(song=song)
        serializer = MusicSerializer(music, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # /api/music/{pk}/sql_cursor_update/
    @action(detail=True, methods=['put'])
    def sql_cursor_update(self, request, pk=None):
        song = request.data.get('song', None)
        if song:
            music = fun_sql_cursor_update(song=song, pk=pk)
            return Response(music, status=status.HTTP_200_OK)

    # /api/music/version_api/
    @action(detail=False, methods=['get'])
    def version_api(self, request):
        music = Music.objects.all()
        if self.request.version == '1.0':
            serializer = MusicSerializerV1(music, many=True)
        else:
            serializer = MusicSerializer(music, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

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

