from unicodedata import name
from django.db import models
from django.contrib.auth.models import AbstractBaseUser ## Exportamos las clases bases utilizadas en django para crear
from django.contrib.auth.models import PermissionsMixin ## usuarios y modificarlos
from django.contrib.auth.models import BaseUserManager

""" Manager para merfiles de usuarios"""
class UserProfileManager(BaseUserManager): 
    def create_user(self, email, name, password = None):
        """ Crea nuevo usuario """
        if not email:
            raise ValueError("El usuario debe tener un email")
        
        email= self.normalize_email(email)
        user = self.model(email=email,name=name)
        
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,name,password):
        user = self.create_user(email,name,password)
        
        user.is_superuser = True
        
        user.is_staff = True
        
        user.save(using=self._db)
        
        return user
    

""" Modelo Base de datos para usuarios en el sistema"""
class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ Modelo Base de datos para ususarios en el sistema """
    email = models.EmailField(unique=True, max_length=255)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects = UserProfileManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    
    def get_full_name(self):
        return self.name
    
    def get_short_name(self):
        return self.name
    
    def __str__(self):
        return self.email