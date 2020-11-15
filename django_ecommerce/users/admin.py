from django.contrib import admin
from .models import UserAddress, Profile


class UserAddressAdmin(admin.ModelAdmin):
    list_display = ['user', 'company', 'phone_number', 'address_1', 'address_2', 'city', 'country', 'postal_code', 'fax']
    list_filter = ['user']


admin.site.register(UserAddress, UserAddressAdmin)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'original_username']
    list_filter = ['user']


admin.site.register(Profile, ProfileAdmin)