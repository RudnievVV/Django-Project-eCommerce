# Generated by Django 3.0 on 2020-02-10 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20200210_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraddress',
            name='address_2',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='company',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='fax',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]