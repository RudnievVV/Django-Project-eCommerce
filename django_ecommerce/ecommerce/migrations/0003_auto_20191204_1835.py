# Generated by Django 3.0 on 2019-12-04 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0002_auto_20191204_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='main_image',
            field=models.ImageField(default='images/product/product_default.jpg', upload_to=''),
        ),
    ]
