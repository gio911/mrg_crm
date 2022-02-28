from django.http import request
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from users.authentication.backends import JWTAuthentication

from .serializers import CategorySerializer
from .models import Category
from rest_framework import permissions
from .permissions import IsOwner

class CategoryListAPIView(ListCreateAPIView):
    serializer_class=CategorySerializer
    queryset=Category.objects.all()
    authentication_classes = (JWTAuthentication,)

    permission_classes=(permissions.IsAuthenticated, IsOwner)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        
        return self.queryset.filter(owner=self.request.user)


class CategoryDetailAPIView(RetrieveUpdateDestroyAPIView):

    serializer_class=CategorySerializer
    queryset=Category.objects.all()
    permission_classes=(permissions.IsAuthenticated,)
    lookup_field="id"

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)        