from django.contrib import admin
from .models import Category, SimpleProduct, SimpleProductAdditionalImage


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'root_category', 'parent_category']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category, CategoryAdmin)


class SimpleProductAdmin(admin.ModelAdmin):
    readonly_fields = ('type',)
    list_display = ['title', 'sku', 'category', 'slug', 'price', 'stock', 'available', 'created_at', 'updated_at']
    list_filter = ['available', 'created_at', 'updated_at']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(SimpleProduct, SimpleProductAdmin)


class SimpleProductAdditionalImageAdmin(admin.ModelAdmin):
    list_filter = ['product']


admin.site.register(SimpleProductAdditionalImage, SimpleProductAdditionalImageAdmin)
