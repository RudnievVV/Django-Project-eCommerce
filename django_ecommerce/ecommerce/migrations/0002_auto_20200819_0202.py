# Generated by Django 3.0.7 on 2020-08-18 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='simpleproduct',
            name='type',
            field=models.CharField(default='Simple', max_length=20),
        ),
    ]
