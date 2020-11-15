from django.db import models
from django.contrib.auth.models import User


# to make the email unique
User._meta.get_field('email')._unique = True


class Profile(models.Model):
    """model for user additional fields"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    original_username = models.CharField(max_length=30, blank=False) # field of original entered username by user during registration, needed to display it in a way user wrote it and not in lowercase


class UserAddress(models.Model):
    """model for each saved user address"""
    user = models.ForeignKey(User, related_name='user_addresses', on_delete=models.CASCADE)
    company = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=25, blank=False)
    address_1 = models.CharField(max_length=150, blank=False)
    address_2 = models.CharField(max_length=150, blank=True)
    city = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=20, blank=False)
    postal_code = models.CharField(max_length=15, blank=False)
    fax = models.CharField(max_length=20, blank=True)