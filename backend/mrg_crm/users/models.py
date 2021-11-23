from django.contrib.auth.models import User
from django.db import models

class Provider(models.Model):
    user = models.OneToOneField(User, related_name='provider_prof', on_delete=models.CASCADE )
    phone = models.CharField(max_length=250, default='')
    rating = models.IntegerField(default=0)
    class Meta:
        verbose_name='Provider'
        verbose_name_plural='Providers'

class Consumer(models.Model):
    user = models.OneToOneField(User, related_name='consumer_prof', on_delete=models.CASCADE )
    phone = models.CharField(max_length=250, default='')
    address = models.TextField(default='')
    geo_location = models.CharField(max_length=250, default='')
    class Meta:
        verbose_name='Consumer'
        verbose_name_plural='Consumers'

