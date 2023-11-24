from rest_framework import serializers
from .models import VideoPost
import re


class VideoPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoPost
        fields = "__all__"
        extra_kwargs = {"owner": {"read_only": True}}

    def __init__(self, *args, owner=None, **kwargs):
        self.owner = owner
        super().__init__(*args, **kwargs)

    def validate(self, data):
        data["owner"] = self.owner
        return super().validate(data)
