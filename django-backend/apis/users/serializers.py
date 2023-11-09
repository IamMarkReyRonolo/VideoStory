from rest_framework import serializers
from .models import User
import re
from utils.bcrypter import Hasher

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def validate(self, attrs):
        if User.objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError({
                'email': ('Email already exists')
            })
        
        if not self.password_must_be_valid(attrs['password']):
            raise serializers.ValidationError({
                'password': ('password is invalid: [a-z], [A-Z], [0-9],[@$!#%*?&], min: 8, max:30')
            })

        if not self.is_valid_email(attrs['email']):
            raise serializers.ValidationError({
                'email': ('Email is invalid')
            })
        
        return super().validate(attrs)
    
    def password_must_be_valid(self, value):
        reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,30}$"
        pat = re.compile(reg)
        mat = re.search(pat, value)
        if mat:
            return True
        return False
    
    def is_valid_email(self, value):
      regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
      if(re.fullmatch(regex, value)):
          return True
      else:
          return False
    
    def create(self, validated_data):
        validated_data['password'] = Hasher().hash_password(validated_data['password'])
        return User.objects.create(**validated_data)