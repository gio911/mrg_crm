from django.http import request
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView
from rest_framework.mixins import ListModelMixin, UpdateModelMixin
from users.authentication.backends import JWTAuthentication
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import CategorySerializer, ProductSerializer, AddProductRequestSerializer
from .models import Category, Product
from rest_framework import permissions, viewsets
from .permissions import IsOwner
from rest_framework.parsers import MultiPartParser, JSONParser
from django.core.files.base import ContentFile
from rest_framework.response import Response
import base64


from drf_yasg.utils import swagger_auto_schema

# from backend.mrg_crm.market import serializers


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
    

class ProductListView(ListModelMixin, GenericAPIView):

    queryset = Product.objects.all().order_by('-id')
    serializer_class = ProductSerializer

    def get_queryset(self):
        pk = self.kwargs['id']
        return self.queryset.filter(owner=self.request.user).filter(category_id=pk)

    def get(self,request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class AddProductView(APIView):
    """
    Adding a new product.
    _____________________
    """
    permission_classes = (IsAuthenticated,)
    parser_classes = (JSONParser,)

    @swagger_auto_schema( 
        request_body = AddProductRequestSerializer, \
        responses={200: ProductSerializer} \
        )
    def post(self, request, format=None):
        print('333', request.data)
        cat = Category.objects.get(pk=request.data.get('category'))
        # subcat = SubCategory.objects.get(pk=request.data.get('subcat'))
        p = Product()
        p.category = cat
        p.owner = request.user
        # p.subcategory = subcat
        p.name = request.data.get('name')
        p.price = request.data.get('price')

        if "image" in request.data:
            p.image = (request.data['image'])

        if "image_base64" in request.data:
            try:
                format, imgstr = request.data.get('image_base64').split(';base64,')
                ext = format.split('/')[-1]
                data = ContentFile(base64.b64decode(imgstr))
                file_name = '%s_user.%s' % (p.id,ext) 
                p.image.save(file_name, data, save=True)
            except:
                pass

        p.save()
        print('777',ProductSerializer(p).data)
        return Response(ProductSerializer(p).data)

    def put(self, request, *args, **kwargs):
        id = kwargs.get('id', None)

        if not id:
            return Response({"error":"Method PUT NOT allowed"})

        try:
            instance = Product.objects.get(id=id)
        except:
            return Response({"error":"Object does not exist"})

        serializer = ProductSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


    def delete(self, request, *args, **kwargs):
        id = kwargs.get('id', None)

        if not id:
            return Response({'error':"Method DELETE not allowed"})

        Product.objects.get(id=id).delete()
        
        return Response({"message":"Product was deleted"})    
    
            