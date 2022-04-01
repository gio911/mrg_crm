from rest_framework import serializers
from . models import Category, Order, OrderProduct, Product

class CategorySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Category
        fields = ['id','name','image',]


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model= Product
        fields = ['id', 'name', 'category', 'price' ]

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance

   

class AddProductRequestSerializer(serializers.Serializer):
    cat = serializers.IntegerField(min_value=1)
    subcat = serializers.IntegerField(min_value=1)
    name = serializers.CharField()
    image = serializers.FileField(allow_empty_file=True, required=False)
    imager_base64 = serializers.CharField(required=False)        

class OrderProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer

    class Meta:
        model=OrderProduct
        fields=['id', 'product', 'amount']
   
class OrderSerializer(serializers.ModelSerializer):

    products = serializers.SerializerMethodField()

    def get_products(self, obj):
        out=[]
        for i in OrderProduct.objects.filter(order=obj):
            out.append(OrderProductSerializer(i).data)

    class Meta:
        model=Order
        fields=['id', 'consumer', 'created_at', 'products']

