from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
import jwt
from datetime import datetime, timedelta
from django.conf import settings
from django.db import models

class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None):
        if username is None:
            raise TypeError('Users should have username')
        if email is None:
            raise TypeError('Email should have username')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password=None):
        if password is None:
            raise TypeError('Password should have username')
        
        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=256, unique=True, db_index=True)
    email = models.CharField(max_length=256, unique=True, db_index=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_stuff = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now_add=True)
    created_at =models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.email
   
    @property
    def token(self):
        return self._generate_jwt_token()

    def get_full_name(self):
        """
        Этот метод требуется Django для таких вещей, как обработка электронной
        почты. Обычно это имя фамилия пользователя, но поскольку мы не
        используем их, будем возвращать username.
        """
        return self.username

    def get_short_name(self):
        """ Аналогично методу get_full_name(). """
        return self.username

    def _generate_jwt_token(self):
        """
        Генерирует веб-токен JSON, в котором хранится идентификатор этого
        пользователя, срок действия токена составляет 1 день от создания
        """
        dt = datetime.now() + timedelta(days=1)

        token = jwt.encode({
            'id': self.pk,
            'exp': int(dt.strftime('%s'))
        }, settings.SECRET_KEY, algorithm='HS256')

        return token.decode('utf-8')


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

