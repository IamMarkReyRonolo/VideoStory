import jwt
from rest_framework import authentication, exceptions
from django.conf import settings
from .models import User


class JWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        auth_data = authentication.get_authorization_header(request)

        if not auth_data:
            return None

        auth_data = auth_data.decode("utf-8").split(" ")

        if len(auth_data) == 2:
            prefix, token = auth_data
            if prefix != "Bearer":
                raise exceptions.AuthenticationFailed("Invalid Authentication Header")
        else:
            raise exceptions.AuthenticationFailed("Invalid Authentication Header")

        try:
            payload = jwt.decode(token, settings.JWT_SECRET_KEY, settings.JWT_ALGORITHM)
            user = User.objects.get(username=payload["username"])
            return (user, token)
        except jwt.DecodeError as e:
            raise exceptions.AuthenticationFailed("Invalid Token")
        except jwt.ExpiredSignatureError as e:
            raise exceptions.AuthenticationFailed("Expired Token")
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed("User not found")
        except Exception as e:
            # Log the exception for troubleshooting, and raise a generic error
            print(f"Unexpected error: {str(e)}")
            raise exceptions.AuthenticationFailed("Authentication failed")
