from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from base.models import VideoPost
from .serializers import VideoPostSerializer

@api_view(['GET'])
def fetch_all_videos(request):
    """
    List all video posts
    """
    videos = VideoPost.objects.all()
    serializer = VideoPostSerializer(videos, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def post_video(request):
    """
    Upload or post a video
    """
    serializer = VideoPostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        message = {
              "message" : "Successfully posted video",
              "video" : serializer.data
        }
        return Response(message, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def video_detail(request, id):
    """
    Retrieve, update or delete a video.
    """
    try:
        video = VideoPost.objects.get(pk=id)
    except VideoPost.DoesNotExist:
        message = {
            "message" : "Video not found"
        }
        return Response(message, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = VideoPostSerializer(video)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = VideoPostSerializer(video, data=request.data)
        if serializer.is_valid():
            serializer.save()
            message = {
              "message" : "Successfully updated video",
              "video" : serializer.data
            }
            return Response(message)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        video.delete()
        message = {
            "message" : "Successfully deleted video"
        }
        return Response(message, status=status.HTTP_204_NO_CONTENT)