from django.db import models
from django.utils import timezone
from django.urls import reverse
from djmoney.models.fields import MoneyField


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True, null=True, db_index=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('title', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product-list-by-category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, null=True, db_index=True)
    description = models.TextField(blank=True)
    description_short = models.TextField(max_length=100, blank=True)
    sku = models.CharField(max_length=100, unique=True)
    price = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
    available = models.BooleanField(default=True)
    stock = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/products/%Y/%m/%d', default='images/product/product_default.jpg', blank=True)

    class Meta:
        ordering = ('title', )
        index_together = (('id', 'slug'),)

    def __str__(self):
        return f"{self.sku} - {self.title}"

    def get_absolute_url(self):
        return reverse('product-detail', args=[self.id, self.slug])