from logging import raiseExceptions
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import  EmailVarificationSerializer, RegisterSerializer, LoginSerializer
import jwt, datetime
from rest_framework import serializers, status, generics
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
import jwt
from django.conf import settings
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from rest_framework import permissions

from .utils import Util

from .models import User


class RegisterView(APIView):

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user_data=serializer.data

        user = User.objects.get(email=user_data['email'])
        token = RefreshToken.for_user(user).access_token
        
        current_site = get_current_site(request).domain
        relativeLink = reverse('email-verify')
        
        absurl = 'http://'+current_site+relativeLink+"?token="+str(token)
        email_body = 'Hi '+user.username+'Use a link below to verify your email\n' +absurl
        data={ 'email_body':email_body, 'to_email':user.email, 'email_subject':'Verify your email'}
        Util.send_email(data)

        return Response(user_data, status=status.HTTP_201_CREATED)



class VerifyEmail(APIView):
    serializer_class=EmailVarificationSerializer

    token_param_config=openapi.Parameter('token', in_=openapi.IN_QUERY, description='Description', type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[token_param_config])
    def get(self, request):
        token = request.GET.get('token')
        print('token', token)
        try:
            print('SECRET_KEY',settings.SECRET_KEY)
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            print('payload', payload)

            user = User.objects.get(id=payload['user_id'])
            print('user', user)

            if not user.is_verified:
                
                user.is_verified = True
                user.save()
            return Response({'email':'Successfully activated'}, status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError as identifire:
            return Response({'error':'Activation Expired'}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as identifier:
            return Response({'error':'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = LoginSerializer
    def post(self, request):
        #print("AUTHORIZATION TOKEN FROM FRONTEND",request.headers['Authorization'])
        print('HIIII THERE', request.META)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)


# class RegisterView(APIView):
#     def post(self, request):
#         serializer=UserSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)




# # class LoginView(APIView):
#     def post(self, request):
#         email=request.data['email']
#         password=request.data['password']

#         user=User.objects.get(email=email)

#         if user is None:
#             raise AuthenticationFailed('User not Found')

#         if not user.check_password(password):
#             raise AuthenticationFailed('Inccorect Password')

#         payload = {
#             'id':user.id,
#             'exp':datetime.datetime.utcnow()+datetime.timedelta(minutes=60),
#             'iat':datetime.datetime.utcnow()
#         }

#         token = jwt.encode(payload,'secret', algorithm='HS256').decode('utf-8')

#         response = Response()

#         response.set_cookie(key='jwt', value=token,httponly=True)
#         response.data={
#             'jwt':token
#         }

#         return response


class UserView(APIView):

    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])

        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)    

        return Response(serializer.data)        

class LogoutView(APIView):
    def post(self,request):
        response=Response()
        response.delete_cookie('jwt')
        response.data={
            'message':'success'
        }    

        return response    