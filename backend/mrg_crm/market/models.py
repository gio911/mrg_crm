from django.db import models
# from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

from users.models import User
from easy_thumbnails.files import get_thumbnailer
from users.models import Consumer, Provider
from mrg_crm.settings import BACKEND_URL


class Category(models.Model):

    name = models.CharField(max_length=250, default='')
    image = models.ImageField(upload_to='category', blank=True, null=True)
    owner = models.ForeignKey(to=User, on_delete = models.CASCADE, 
                        related_name='categories')

    class Meta:
        verbose_name='Category'
        verbose_name_plural='Categories'

    def __str__(self):
        return self.name    

    @property
    def image_url(self):
        return BACKEND_URL + self.image.url

    @property
    def get_small_image_url(self):
        return BACKEND_URL + get_thumbnailer(self.image).get_thumbnail({
            'size':(100, 100)
        }).url

    @property
    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50"/>' % self.image.url)


class Product(models.Model):
    name = models.CharField(max_length=250, default='')
    price = models.DecimalField(max_digits=10, decimal_places=2, max_length=255, blank=True, null=True)
    description=models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='product', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True, related_name='products')
    owner = models.ForeignKey(to=User, on_delete = models.CASCADE, blank=True, null=True )
    
    class Meta:
        verbose_name='Product'
        verbose_name_plural='Products'  

    @property
    def get_small_image_url(self):
        return BACKEND_URL + get_thumbnailer(self.image).get_thumbnail({
            'size':(100, 100)
        }).url

    def __str__(self):
        return f"{self.name} ({self.category})"  



class Store(models.Model):
    provider = models.ForeignKey(Provider, on_delete = models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete = models.CASCADE, blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    class Meta:
        verbose_name='Store'
        verbose_name_plural='Stores'

class Order(models.Model):

    STATUS = (
        ('new', 'new order'),
        ('pending', 'pending order'),
        ('finishing', 'finished order'),
    )

    consumer = models.ForeignKey(Consumer, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)    
    update_at = models.DateTimeField(auto_now=True)  
    status = models.CharField(max_length=10, default = 'new', choices=STATUS)  
    class Meta:
        verbose_name='Order'
        verbose_name_plural='Orders'

class OrderProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null = True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null = True, blank=True)    
    ammount = models.IntegerField(default=0)
    class Meta:
        verbose_name='OrderProduct'
        verbose_name_plural='OrderProducts'

        