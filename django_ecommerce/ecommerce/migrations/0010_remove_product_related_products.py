# Generated by Django 3.0 on 2019-12-06 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0009_auto_20191206_1719'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='related_products',
        ),
    ]