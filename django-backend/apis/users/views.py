from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import User
from .serializers import UserSerializer
from utils.bcrypter import Hasher
from utils.authenticator import JWTAuthentication, JWT_SECRET
import jwt



@api_view(['GET'])
def get_all_users(request):
    """
    Get all users
    """
    payload, token = JWTAuthentication().authenticate(request)
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def register_user(request):
    """
    Create a user account
    """
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        message = {
              "message" : "Successfully created account",
              "user" : serializer.data
        }
        return Response(message, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login_user(request):
    """
    Login a user account
    """
    data = request.data
    email = data.get('email', '')
    password = data.get('password', '')

    try:
        user = User.objects.get(email=email)
        verified = Hasher().verify_password(login_password=password, original_password=user.password)

        if verified:
            if user:
                auth_token = jwt.encode(
                    {'email': email,
                    'id': user.id,
                    'name': user.first_name + " " + user.last_name},
                    JWT_SECRET
                )
                serializer = UserSerializer(user)
                data =  {
                    "message" : "Successfully logged in",
                    "user" : serializer.data,
                    "token" : auth_token
                }

                return Response(data, status=status.HTTP_200_OK)

        return Response({'message':'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        if 'User matching query does not exist.' in str(e):
            return Response({'message':'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET','PUT', 'DELETE'])
def view_edit_user(request, id):
    """
    Retrieve, update or delete a user.
    """
    payload, token = JWTAuthentication().authenticate(request)
    try: 
        user = User.objects.get(pk=id)
    except User.DoesNotExist:
        message = {
            "message" : "User not found"
        }
        return Response(message, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            message = {
              "message" : "Successfully updated user",
              "user" : serializer.data
            }
            return Response(message)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        message = {
            "message" : "Successfully deleted user"
        }
        return Response(message, status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET'])
def get_user_data(request):
    """
    Retrieve, update or delete a user.
    """
    payload, token = JWTAuthentication().authenticate(request)
    try: 
        user = User.objects.get(pk=payload['id'])
        serializer = UserSerializer(user)
        return Response(serializer.data)
    except User.DoesNotExist:
        message = {
            "message" : "User not found"
        }
        return Response(message, status=status.HTTP_404_NOT_FOUND)

        
        
        
    



