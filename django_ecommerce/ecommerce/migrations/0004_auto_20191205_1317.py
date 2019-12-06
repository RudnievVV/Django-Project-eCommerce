# Generated by Django 3.0 on 2019-12-05 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0003_auto_20191204_1835'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='item',
        ),
        migrations.AddField(
            model_name='cart',
            name='cart_items',
            field=models.ManyToManyField(to='ecommerce.Product'),
        ),
    ]