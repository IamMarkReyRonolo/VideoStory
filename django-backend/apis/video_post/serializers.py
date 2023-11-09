from rest_framework import serializers
from .models import VideoPost
import re

class VideoPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoPost
        fields = '__all__'