from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from django.utils.translation import gettext_lazy as _

# Choices for the role field


class User(AbstractUser):
    username = None
    name = models.CharField(max_length=20,null=True, blank=True)
    email = models.EmailField(_('email address'), unique=True)
    company = models.CharField(blank=True, max_length=50)
    address = models.CharField(blank=True, max_length=50)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    class Meta:
        db_table = 'db_users'
        # verbose_name = "Authentications & Authorizations"   #For Showing this text as to admin panel
        # verbose_name_plural = "Authentications & Authorizations"

    def __str__(self):
        return self.email