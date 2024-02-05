from django.db import models
from user.managers import UserManager
from v1.models import DefaultAbstract
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin



""" 
Prayekt uchun User modeli AbstractBaseUser va PermissionsMixin dan vorislik olib email orqali login registratsiya ya'ni email > unique bo'lish kk
"""

class  User(AbstractBaseUser, PermissionsMixin, DefaultAbstract):
    email = models.EmailField(max_length=50, unique=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)


    def __str__(self) -> str:
        return f"{self.email} - {self.first_name}"




    objects = UserManager()

    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

