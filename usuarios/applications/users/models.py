from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserManager

# Create your models here.
class User(AbstractBaseUser,PermissionsMixin):
    GENERO_CHOICES=(
        ('F','Femenino'),
        ('M','Masculino'),
        ('O','Otros'),
    )
    
    username=models.CharField(max_length=10,unique=True)
    nombres=models.CharField(max_length=30,blank=True)
    apellidos=models.CharField(max_length=30,blank=True)
    email=models.EmailField()
    genero=models.CharField(max_length=1,choices=GENERO_CHOICES,blank=True)
    is_staff=models.BooleanField(default=False)
    
    USERNAME_FIELD='username'
    
    REQUIRED_FIELDS=['email',]
    
    objects=UserManager()
    
    def getShortName(self):
        return self.username
    
    def getFullName(self):
        return self.nombres+" "+self.apellidos