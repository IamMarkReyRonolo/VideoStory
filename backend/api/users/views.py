from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes,
)
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from .serializers import UserSerializer, LoginSerializer, UpdatedUserDetailsSerializer
from drf_yasg.utils import swagger_auto_schema
from .models import User
import jwt
from django.conf import settings
from api.users.customauth import JWTAuthentication
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


@swagger_auto_schema(method="POST", request_body=UserSerializer)
@api_view(["POST"])
@permission_classes([AllowAny])
def register_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

        # encrypt password
        user = User.objects.get(username=serializer.data["username"])
        user.set_password(serializer.data["username"])
        user.save()
        response = {"message": "Successfully added user", "user": serializer.data}
        return Response(response, status=201)
    return Response(serializer.errors, status=400)


@swagger_auto_schema(method="POST", request_body=LoginSerializer)
@api_view(["POST"])
@permission_classes([AllowAny])
def login_user(request):
    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(username=username, password=password)

    if user is not None:
        auth_token = jwt.encode(
            {
                "username": username,
                "id": user.id,
                "name": user.first_name + " " + user.last_name,
            },
            settings.JWT_SECRET_KEY,
        )
        serializer = UserSerializer(user)
        response_data = {
            "message": "Successfully logged in",
            "user": serializer.data,
            "access_token": str(auth_token),
        }
        return Response(response_data)
    else:
        return Response({"error": "Invalid credentials"}, status=400)


@api_view(["GET"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_user_data(request):
    """
    Retrieve a user.
    """
    try:
        user_id = request.user.id
        user = User.objects.get(pk=user_id)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    except User.DoesNotExist:
        message = {"message": "User not found"}
        return Response(message, status=status.HTTP_404_NOT_FOUND)


@api_view(["GET"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def fetch_specific_user_by_id(request, id):
    """
    Retrieve a user.
    """
    try:
        user = User.objects.get(pk=id)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    except User.DoesNotExist:
        message = {"message": "User not found"}
        return Response(message, status=status.HTTP_404_NOT_FOUND)


@swagger_auto_schema(method="PUT", request_body=UpdatedUserDetailsSerializer)
@api_view(["PUT"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def update_user_by_id(request, id):
    """
    Update a user.
    """
    try:
        user = User.objects.get(pk=id)
        serializer = UpdatedUserDetailsSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            message = {
                "message": "Successfully updated user",
                "user": serializer.data,
            }
            return Response(message)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except User.DoesNotExist:
        message = {"message": "User not found"}
        return Response(message, status=status.HTTP_404_NOT_FOUND)


@api_view(["DELETE"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete_user_by_id(request, id):
    """
    Delete a user.
    """
    try:
        user = User.objects.get(pk=id)
        user.delete()
        message = {"message": "Successfully deleted user"}
        return Response(message, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        message = {"message": "USer not found"}
        return Response(message, status=status.HTTP_404_NOT_FOUND)
