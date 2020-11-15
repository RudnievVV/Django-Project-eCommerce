from django.contrib import admin
from .models import UserAddress


class UserAddressAdmin(admin.ModelAdmin):
    list_display = ['user', 'company', 'phone_number', 'address_1', 'address_2', 'city', 'country', 'postal_code', 'fax']
    list_filter = ['user']


admin.site.register(UserAddress, UserAddressAdmin)