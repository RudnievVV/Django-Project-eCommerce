# Generated by Django 3.0 on 2020-03-14 22:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0012_auto_20191211_1118'),
        ('orders', '0002_auto_20200315_0037'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OrderItems',
            new_name='OrderItem',
        ),
    ]