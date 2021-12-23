# from rest_framework import serializers, viewsets, permissions

# from market.views1.product import ProductSerializer
# from .. models import Category, SubCategory

# class CategorySerializer(serializers.HyperlinkedModelSerializer):
#     products=ProductSerializer( many=True)
#     class Meta:
#         model = Category
#         depth = 1
#         fields = ['id', 'name', 'image_url', 'get_small_image_url', 'products']

# class SubCategorySerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = SubCategory
#         fields = ['id', 'name']

# class CategoryViewSet(viewsets.ModelViewSet):
#     """
#             API endpoint that allows users to read and modify categories
#     """        

#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#     permission_classes = [permissions.AllowAny]
#     http_method_names = ['get', 'post']