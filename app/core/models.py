from django.db import models
from django.contrib import admin
from django.contrib.auth.models import  AbstractBaseUser, BaseUserManager, \
                                        PermissionsMixin
# Create your models here.
class userManager(BaseUserManager):
    """docstring for userManager."""

    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new User"""
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user


    def create_superuser(self, email, password):
        """Creates and saves a new super user"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

class User(AbstractBaseUser,PermissionsMixin):
    """Custom user model that supports user emial instead of username"""
    email = models.EmailField(max_length=255,unique=True)
    name= models.CharField(max_length=255)
    is_admin = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = userManager()

    USERNAME_FIELD = 'email'
