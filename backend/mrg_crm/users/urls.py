from django.urls import path
from .views import LoginAPIView, LogoutView, RegisterView, UserView, VerifyEmail
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )


urlpatterns=[
    #http://localhost:8000/api/register
    path('register/', RegisterView.as_view(), name="register"),
    path('email-verify/', VerifyEmail.as_view(), name="email-verify" ),
    #http://localhost:8000/api/login 
    path('login/', LoginAPIView.as_view(), name='login'),
    #http://localhost:8000/api/user 
    path('user/', UserView.as_view()),
    #http://localhost:8000/api/logout 
    path('logout/', LogoutView.as_view())


]