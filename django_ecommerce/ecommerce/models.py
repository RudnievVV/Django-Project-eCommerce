from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.conf import settings
from djmoney.models.fields import MoneyField
import datetime


def product_main_image_directory_path(instance, filename): # needed to define product folder to save main image
    return f'img/product/{instance.sku}/{filename}'

def product_additional_image_directory_path(instance, filename): # needed to define product folder to save additional images
    return f'img/product/{instance.product.sku}/{filename}'


class Category(models.Model):
    """category that can be assigned to product"""
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True, null=True, db_index=True)
    new = models.BooleanField(default=True) # used to define if to show "new" label on front-end or not
    root_category = models.BooleanField(default=True) # if False, it won't be displayed in megamenu
    parent_category = models.ForeignKey('self', related_name='sub_categories', null=True, blank=True, on_delete=models.CASCADE) # shouldn't be selected within True root_category
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('title', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.title

    def products_inside(self):
        products_inside_category = SimpleProduct.objects.filter(category=self, available=True).first() 
        """here is needed to list all existing product models
        based on BaseProduct abstract model in order to have correctly counted
        products inside category""" 
        if products_inside_category:
            return True
        return False

    def get_absolute_url(self):
        return reverse('category-page', args=[self.slug])


class BaseProduct(models.Model):
    """abstract Base Product model"""
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, null=True, db_index=True)
    description = models.TextField(blank=True)
    description_short = models.TextField(max_length=100, blank=True)
    sku = models.CharField(max_length=100, unique=True)
    brand = models.CharField(max_length=30, unique=False, default='Undefined')
    price = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
    available = models.BooleanField(default=True)
    new = models.BooleanField(default=True) # that field will be used to show or not "new" label on product
    on_sale = models.BooleanField(default=False) # that field will be used to show or not "on sale" label on product
    stock = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    main_image = models.ImageField(upload_to=product_main_image_directory_path, default=settings.PRODUCT_DEFAULT_IMAGE)

    class Meta:
        ordering = ('title', )
        abstract = True

    def __str__(self):
        return f"{self.sku} - {self.title}"

    def get_absolute_url(self):
        return reverse('product-page', args=[self.sku])

    def new_status(self, days_to_display_new_status=settings.DAYS_TO_DEFINE_PRODUCT_NEW_STATUS):
        time_after_creation = datetime.datetime.now(timezone.utc) - self.created_at
        if time_after_creation.days <= days_to_display_new_status and self.new:
            return True
        return False


class SimpleProduct(BaseProduct):
    """simple product model"""
    type = models.CharField(max_length=20, default='Simple')


class SimpleProductAdditionalImage(models.Model):
    """product additional image"""
    product = models.ForeignKey(SimpleProduct, related_name='product_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=product_additional_image_directory_path, default=settings.PRODUCT_DEFAULT_IMAGE)

    def __str__(self):
        return f"{self.product.title} | {self.product.sku} | {self.id}"