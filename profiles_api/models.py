from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


# Create your models here.
class  UserProfileManager(BaseUserManager):
    """Manager For User Profiles """
    def create_user(self, email, name, password=None):
        """Create a new user Profile """
        if not email:
            raise ValueError("User Must Have an Email Address")

        email = self.normalize_email(email)
        user = self.model(email = email , name = name)

        user.Set_password(password)
        user.Save(using=self_.db)
        return user

    def create_superuser(self, email, name, password):
        """Create and Save a new super user with given details"""
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self_.db)
        return user


class UserProfile(AbstractBaseUser,PermissionsMixin):
    """Database Model for Users in the System"""
    email = models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def get_full_name(self):
        """Get Full Name of User """
        return self.name

    def get_short_name(self):
        """Get Short Name for User """
        return self.name

    def __str__(self):
        """String presentation of the User"""
        return self.email
