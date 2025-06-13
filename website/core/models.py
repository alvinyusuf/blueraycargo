from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Country(models.Model):
    country_name = models.CharField(max_length=100)
    country_flag = models.URLField()
    country_currency = models.CharField(max_length=10)

    def __str__(self):
        return self.country_name

class Category(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    category_title = models.CharField(max_length=100)
    price_per_kilo = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.category_title} ({self.country.country_name})"

