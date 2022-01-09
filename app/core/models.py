from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
    PermissionsMixin  # This classes extends User Model


class UserManager(BaseUserManager):  # Use () to extends class

    # Use ** for extra parameters
    def create_user(self, email, password=None, **extra_fields):
        """Create and saves a new user"""

        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)  # Use using=self._db for multiple databases

        return user

    def create_superuser(self, email, password):
        """Creates and saves a new super user"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()  # Assign UserManager() to object attribute

    USERNAME_FIELD = 'email'  # attribute (user_name is the default value)

# Se edita settings.py se agrega AUTH_USER_MODEL = 'core.User'
# Finalmente se corren las migraciones
