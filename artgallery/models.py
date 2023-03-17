from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from .managers import CustomUserManager
from django.template.defaultfilters import slugify


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True, error_messages={'required': 'Почта не указана'}) 
    name = models.CharField(max_length=20, error_messages={'required': 'Имя не указано'})
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='profile_image', blank=True)
    background_image = models.ImageField(upload_to = 'background-user_image', blank=True)
    bill_number = models.IntegerField(null=True, blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()
    def __str__(self):
        return self.email

    


class Works(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    category = models.TextField()
    photo = models.ImageField(upload_to='works_image')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    autor = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    like = models.ManyToManyField(CustomUser, related_name='work_one')


    def total_likes(self):
        return self.like.count()


class Request(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(_('email address'), unique=False)
    message = models.TextField()


class Likes(models.Model):
    work = models.ForeignKey(Works, on_delete=models.CASCADE, related_name="likes")            
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="likes")


class Meta:
    constraints = [
        models.UniqueConstraint(fields=['user', 'work'], name="unique_like"),
    ]

