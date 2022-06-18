from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


# Create your models here.
#TODO:Create urls to get shopdetails
class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("users must have an email address")
        if not username:
            raise ValueError("users must have a username")
        user = self.model(
            email=self.normalize_email(email),
            username=username
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class ShopName(models.Model):
    coffee_shop_id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=60)
    location = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Account(AbstractBaseUser):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True, primary_key=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    role = models.CharField(max_length=10)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = MyAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class ProfileInfo(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE, null=False, blank=False, unique=True)
    profile = models.ImageField(null=True, blank=True)
    contact = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    shopName = models.ForeignKey(ShopName, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.user.name


class Coffee(models.Model):
    name = models.CharField(max_length=60, unique=True, primary_key=True)
    image = models.ImageField(null=False, blank=False)
    ratings = models.DecimalField(max_digits=3, decimal_places=2)
    taste = models.CharField(max_length=60)
    coffeeType = models.CharField(max_length=60)
    description = models.TextField()
    price = models.IntegerField()
    totalUser = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)
    shopName = models.ForeignKey(ShopName, on_delete=models.CASCADE, null=False, blank=False)
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.name[0:50]

    class Meta:
        ordering = ['-updated_at']


class RecommendedCoffee(models.Model):
    recommend = models.OneToOneField(Coffee, on_delete=models.CASCADE, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.recommend.name[0:50]

    class Meta:
        ordering = ['-created_at']


class IsFavourite(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=False, blank=False)
    favourite = models.BooleanField(default=False)
    coffee = models.ForeignKey(Coffee, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.coffee.name


class Order(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=False, blank=False)
    coffee_id = models.ForeignKey(Coffee, on_delete=models.CASCADE, null=False, blank=False)
    name = models.CharField(max_length=200)
    size = models.CharField(max_length=10)
    quantity = models.IntegerField()
    shop_name = models.ForeignKey(ShopName, on_delete=models.CASCADE, null=False, blank=False)
    address = models.CharField(max_length=200)
    contact = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-updated_at']
