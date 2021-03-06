# Generated by Django 2.0.5 on 2018-05-24 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='hirer_address',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='contact'),
        ),
        migrations.AlterField(
            model_name='event',
            name='hirer_email',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='contact'),
        ),
        migrations.AlterField(
            model_name='event',
            name='hirer_mobile',
            field=models.IntegerField(blank=True, null=True, verbose_name='mobile'),
        ),
        migrations.AlterField(
            model_name='event',
            name='hirer_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='contact'),
        ),
        migrations.AlterField(
            model_name='event',
            name='hirer_phone',
            field=models.IntegerField(blank=True, null=True, verbose_name='phone'),
        ),
        migrations.AlterField(
            model_name='event',
            name='hirer_postcode',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='contact'),
        ),
    ]
