from rest_framework import serializers
from . models import Category, Order, OrderProduct, Product

class CategorySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Category
        fields = ['id','name','image',]

class OrderSerializer(serializers.ModelSerializer):

    products = serializers.SerializerMethodField()


    def get_products(self, obj):
        out=[]
        for i in OrderProduct.objects.filter(order=obj):
            print('iiiiiiiiii',i)
            out.append(OrderProductSerializer(i).data)
        print('1111111', out)
        return out 

    class Meta:
        model=Order
        fields=['id', 'consumer', 'created_at', 'products']

class AddProductRequestSerializer(serializers.Serializer):
    cat = serializers.IntegerField(min_value=1)
    subcat = serializers.IntegerField(min_value=1)
    name = serializers.CharField()
    image = serializers.FileField(allow_empty_file=True, required=False)
    imager_base64 = serializers.CharField(required=False)        

class ProductSerializer(serializers.ModelSerializer):

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance

    class Meta:
        model= Product
        fields = ['id', 'name', 'category', 'price' ]    

class OrderProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer
    order = OrderSerializer

    class Meta:
        model=OrderProduct
        fields=['id','order', 'amount', 'product', 'price' ]
   


