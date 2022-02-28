from django.urls import path
from .views import LoginAPIView, LogoutView, RegistrationAPIView, UserView, VerifyEmail



urlpatterns=[
    #http://localhost:8000/api/register
    path('register/', RegistrationAPIView.as_view(), name="register"),
    path('email-verify/', VerifyEmail.as_view(), name="email-verify" ),
    #http://localhost:8000/api/login 
    path('login/', LoginAPIView.as_view(), name='login'),
    #http://localhost:8000/api/user 
    path('user/', UserView.as_view()),
    #http://localhost:8000/api/logout 
    path('logout/', LogoutView.as_view())


]