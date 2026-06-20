from rest_framework import serializers
from mytest.models import Music

class ToUpperCaseCharField(serializers.CharField):
    def to_representation(self, value):
        return value.upper()

class MusicSerializer(serializers.ModelSerializer):
    singer = ToUpperCaseCharField()

    class Meta:
        model = Music
        # fields = '__all__'  全部 fields
        fields = ('id', 'song', 'singer', 'last_modify_date', 'created')