from rest_framework.response import Response
from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes,
)
from rest_framework import status
from .models import VideoPost
from .serializers import VideoPostSerializer
from api.users.customauth import JWTAuthentication
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework import pagination
from drf_yasg import openapi


class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 1000


@swagger_auto_schema(
    method="GET",
    manual_parameters=[
        openapi.Parameter(
            "page",
            openapi.IN_QUERY,
            description="Specify the page number",
            type=openapi.TYPE_INTEGER,
        ),
        openapi.Parameter(
            "page_size",
            openapi.IN_QUERY,
            description="Specify the size per page",
            type=openapi.TYPE_INTEGER,
        ),
    ],
)
@api_view(["GET"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def fetch_all_videos(request):
    """
    List all video posts
    """
    paginator = StandardResultsSetPagination()
    paginator.page_size = request.query_params.get("page_size", paginator.page_size)

    videos = VideoPost.objects.filter(owner=request.user.id)
    result_page = paginator.paginate_queryset(videos, request)
    serializer = VideoPostSerializer(result_page, many=True)
    response = {
        "page_num": paginator.page.number,
        "page_size": paginator.page.paginator.per_page,
        "count": paginator.page.paginator.count,
        "next": paginator.get_next_link(),
        "previous": paginator.get_previous_link(),
        "results": serializer.data,
    }

    return Response(response, status=status.HTTP_200_OK)


@swagger_auto_schema(method="POST", request_body=VideoPostSerializer)
@api_view(["POST"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def post_video(request):
    """
    Upload or post a video
    """
    data = request.data
    serializer = VideoPostSerializer(data=data, owner=request.user)

    if serializer.is_valid():
        serializer.save()
        message = {"message": "Successfully posted video", "video": serializer.data}
        return Response(message, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def fetch_specific_video_by_id(request, id):
    """
    Retrieve a video.
    """
    try:
        video = VideoPost.objects.get(pk=id, owner=request.user.id)
        serializer = VideoPostSerializer(video)
        return Response(serializer.data)
    except VideoPost.DoesNotExist:
        message = {"message": "Video not found"}
        return Response(message, status=status.HTTP_404_NOT_FOUND)


@swagger_auto_schema(method="PUT", request_body=VideoPostSerializer)
@api_view(["PUT"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def update_video_by_id(request, id):
    """
    Update a video.
    """
    try:
        video = VideoPost.objects.get(pk=id, owner=request.user.id)
        serializer = VideoPostSerializer(video, data=request.data, owner=request.user)
        if serializer.is_valid():
            serializer.save()
            message = {
                "message": "Successfully updated video",
                "video": serializer.data,
            }
            return Response(message)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except VideoPost.DoesNotExist:
        message = {"message": "Video not found"}
        return Response(message, status=status.HTTP_404_NOT_FOUND)


@api_view(["DELETE"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete_video_by_id(request, id):
    """
    Delete a video.
    """
    try:
        video = VideoPost.objects.get(pk=id, owner=request.user.id)
        video.delete()
        message = {"message": "Successfully deleted video"}
        return Response(message, status=status.HTTP_200_OK)
    except VideoPost.DoesNotExist:
        message = {"message": "Video not found"}
        return Response(message, status=status.HTTP_404_NOT_FOUND)
