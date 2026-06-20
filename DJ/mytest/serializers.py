from rest_framework import serializers
from mytest.models import Music


class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        # fields = '__all__'  全部 fields
        fields = ('id', 'song', 'singer', 'last_modify_date', 'created')