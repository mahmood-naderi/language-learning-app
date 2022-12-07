from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_("email is empty"))
        email = self.normalize_email(email)
        user = User(email = email, **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("is_staff must be True"))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("is_superuser must be True"))
        
        return self.create_user(email, password, **extra_fields)
        


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length = 255, unique = True)
    name = models.CharField(max_length = 25)
    is_staff = models.BooleanField(default = False)
    created_date = models.DateField(auto_now_add = True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return self.email