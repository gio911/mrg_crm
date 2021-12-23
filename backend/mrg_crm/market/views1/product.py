# from django.db.models.query import QuerySet
# from rest_framework.generics import GenericAPIView
# from rest_framework.mixins import ListModelMixin
# from rest_framework import serializers

# # from market.views.category import CategorySerializer

# from market.models import Product
# from market.filters import ProductFilter

# class ProductSerializer(serializers.ModelSerializer):
#     # category = CategorySerializer()
#     # subcategory = SubCategorySerializer()
#     class Meta:
#         model = Product
#         fields = ['id', 'name', 'get_small_image_url',]

# class ProductListView(ListModelMixin, GenericAPIView):
#     queryset = Product.objects.all()
#     serializer_class =ProductSerializer
#     filter_class = ProductFilter

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
