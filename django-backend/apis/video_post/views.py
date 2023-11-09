from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import VideoPost
from .serializers import VideoPostSerializer
from lib.authenticator import JWTAuthentication


@api_view(['GET'])
def fetch_all_videos(request):
    """
    List all video posts
    """
    payload, token = JWTAuthentication().authenticate(request)
    videos = VideoPost.objects.filter(owner=payload['id'])
    serializer = VideoPostSerializer(videos, many=True)
    payload = {
        "videos": serializer.data
    }
    return Response(payload)


@api_view(['POST'])
def post_video(request):
    """
    Upload or post a video
    """
    payload, token = JWTAuthentication().authenticate(request)
    data = request.data
    data['owner'] = payload['id']

    serializer = VideoPostSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        message = {
              "message" : "Successfully posted video",
              "video" : serializer.data
        }
        return Response(message, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def view_edit_video(request, id):
    """
    Retrieve, update or delete a video.
    """
    payload, token = JWTAuthentication().authenticate(request)
    try:
        video = VideoPost.objects.get(pk=id, owner=payload['id'])
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