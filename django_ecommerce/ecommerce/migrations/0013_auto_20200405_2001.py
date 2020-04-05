# Generated by Django 3.0 on 2020-04-05 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0012_auto_20191211_1118'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductAdditionalImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='images/product/product_default.jpg', upload_to='images/product/%Y/%m/%d')),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.AddField(
            model_name='product',
            name='main_image',
            field=models.ImageField(default='images/product/product_default.jpg', upload_to='images/product/%Y/%m/%d'),
        ),
    ]
