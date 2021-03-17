from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.utils import timezone


class CustomAccountManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """creates a new user"""

        if not email:
            raise ValueError('Account must contain an email address!')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """creates a new admin"""

        admin_user = self.create_user(email, password)
        admin_user.is_staff = True
        admin_user.is_superuser = True
        admin_user.save()

        return admin_user


class Account(AbstractBaseUser, PermissionsMixin):
    """creates account model by editing django user model"""

    email = models.EmailField(max_length=100, unique=True)
    username = models.CharField(max_length=60)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    timestamp = models.DateTimeField(default=timezone.now)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
