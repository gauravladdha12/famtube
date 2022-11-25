from rest_framework import serializers
from famfetch.models import videos

class VideosSerializer(serializers.ModelSerializer):
    class Meta:
        model = videos
        fields = '__all__'