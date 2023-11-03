from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import VideoPost
from .serializers import VideoPostSerializer

@api_view(['GET'])
def fetch_all_videos(request):
    videos = VideoPost.objects.all()
    serializer = VideoPostSerializer(videos, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def post_video(request):
    print(request.data)
    serializer = VideoPostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)