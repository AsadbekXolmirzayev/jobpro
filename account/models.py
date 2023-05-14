from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.db.models.signals import pre_save, post_save
from rest_framework_simplejwt.tokens import RefreshToken
from django.conf import settings

Profile = settings.AUTH_USER_MODEL


class ProfileManager(BaseUserManager):

    def create_user(self, username, password=None, **extra_fields):
        if username is None:
            return TypeError('User should have username!')

        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        if password is None:
            raise TypeError('Password should not be None')

        user = self.create_user(
            username=username,
            password=password,
            **extra_fields,
        )
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.role = 2
        user.save(using=self._db)
        return user


class Country(models.Model):
    title = models.CharField(max_length=225)

    def __str__(self):
        return self.title


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city = models.CharField(max_length=225)

    def __str__(self):
        return f'{self.city}, {self.country.title}'


class Company(models.Model):
    title = models.CharField(max_length=225)

    def __str__(self):
        return self.title


class Account(AbstractBaseUser, PermissionsMixin):

    ROLE = (
        (0, "HR"),
        (1, "Candidate"),
        (2, "Admin"),
    )
    username = models.CharField(max_length=60, unique=True, verbose_name='Username', db_index=True)
    first_name = models.CharField(max_length=60, verbose_name='First name', null=True)
    last_name = models.CharField(max_length=60, verbose_name='Last name', null=True)
    avatar = models.ImageField(upload_to='account/')
    bio = models.TextField()
    role = models.IntegerField(choices=ROLE, default=0)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    is_superuser = models.BooleanField(default=False, verbose_name='Super user')
    is_staff = models.BooleanField(default=False, verbose_name='Staff user')
    is_active = models.BooleanField(default=True, verbose_name='Active user')
    created_date = models.DateTimeField(auto_now_add=True)

    objects = ProfileManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        if self.first_name and self.last_name:
            return f'{self.last_name} {self.first_name}'
        return f'{self.username}'

    @property
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
        return data


def account_post_save(instance, sender, *args, **kwargs):
    if instance.role == 2:
        instance.is_staff = True
    else:
        instance.is_staff = False
    return instance


post_save.connect(account_post_save, sender=Account)
