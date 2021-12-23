from django.urls.base import translate_url
from .models import User
from rest_framework import serializers
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed



class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password']

    def validate(self, attrs):
        email = attrs.get('email', '')
        username = attrs.get('username', '')

        if not username.isalnum():
            raise serializers.ValidationError('The User should only contains alphanumeric characters')
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class EmailVarificationSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=555)

    class Meta:
        model=User
        fields=['token']

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=3)
    password = serializers.CharField(max_length=68, min_length=6, write_only=True) 
    username = serializers.EmailField(max_length=255, min_length=3, read_only=True)
    tokens = serializers.SerializerMethodField()

    def get_tokens(self, obj):

        user = User.objects.get(email=obj['email'])

        #print('TOKENS DATA', user.tokens()['access'],user.tokens()['refresh'])

        return {
            'access':user.tokens()['access'],
            'refresh':user.tokens()['refresh']
        }
    
    class Meta:
        model=User
        fields=['email', 'password', 'username', 'tokens']

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')
        user = auth.authenticate(email=email, password=password)
        
        if not user:
            raise AuthenticationFailed('Invalid credantials, try again')
        if not user.is_active:
            raise AuthenticationFailed('Account desable')
        if not user.is_verified:
            raise AuthenticationFailed('Email is not verified')    
        
        
        return {
            
            'email':user.email,
            'username':user.username,
            'tokens':user.tokens
        }

              

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'email', 'password']
#         extra_kwargs = {
#             'password':{'write_only':True}
#         }


#     def create(self, validated_data):
#         password = validated_data.pop('password', None)
#         instance = self.Meta.model(**validated_data)
#         if password is not None:
#             instance.set_password(password)
#         instance.save()
#         return instance    
