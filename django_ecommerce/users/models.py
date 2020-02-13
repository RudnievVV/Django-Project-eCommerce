from django.db import models
from django.contrib.auth.models import User
from PIL import Image


User._meta.get_field('email')._unique = True


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='images/user/default.jpg', upload_to='images/user/profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class UserAddress(models.Model):
    user = models.ForeignKey(User, related_name='user_addresses', on_delete=models.CASCADE)
    company = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=25, blank=False)
    address_1 = models.CharField(max_length=150, blank=False)
    address_2 = models.CharField(max_length=150, blank=True)
    city = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=20, blank=False)
    postal_code = models.CharField(max_length=15, blank=False)
    fax = models.CharField(max_length=20, blank=True)
