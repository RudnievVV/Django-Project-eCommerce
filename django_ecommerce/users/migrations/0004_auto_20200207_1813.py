# Generated by Django 2.2.4 on 2020-02-07 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200207_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraddress',
            name='address_1',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='address_2',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='city',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='company',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='country',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='fax',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='phone_number',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='postal_code',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
