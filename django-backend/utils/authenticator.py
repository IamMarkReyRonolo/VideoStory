import jwt
from dotenv import load_dotenv
from rest_framework import authentication, exceptions
from apis.users.models import User
import os

load_dotenv()
JWT_SECRET = os.getenv('JWT_SECRET')
JWT_ALGORITHM = os.getenv('JWT_ALGORITHM')

class JWTAuthentication(authentication.BasicAuthentication):

    def authenticate(self, request):
        auth_data = authentication.get_authorization_header(request)
        if not auth_data:
            raise exceptions.AuthenticationFailed('Unauthenticated')
        
        prefix, token = auth_data.decode('utf-8').split(' ')
        print(token)
        print(prefix)
        try:
            payload = jwt.decode(token, JWT_SECRET, algorithms=JWT_ALGORITHM)
            return payload, token
        except jwt.DecodeError as e:
            print(e)
            raise exceptions.AuthenticationFailed('Invalid Token')
        except jwt.ExpiredSignatureError as e:
            raise exceptions.AuthenticationFailed('Expired Token')