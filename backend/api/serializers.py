from rest_framework import serializers
from base.models import VideoPost

class VideoPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoPost
        fields = '__all__'