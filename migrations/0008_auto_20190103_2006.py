# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-01-03 20:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0007_auto_20181022_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='hirer_mobile',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='mobile'),
        ),
        migrations.AlterField(
            model_name='event',
            name='hirer_phone',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='phone'),
        ),
    ]