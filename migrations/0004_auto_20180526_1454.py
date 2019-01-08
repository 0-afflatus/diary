# Generated by Django 2.0.5 on 2018-05-26 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0003_auto_20180524_1543'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='featured_img',
            field=models.ImageField(blank=True, help_text='600 * 800 pixel image.', upload_to='uploads/'),
        ),
        migrations.AddField(
            model_name='event',
            name='realm_slug',
            field=models.SlugField(blank=True, help_text='URL friendly name; lowercase, numbers and underscores only.', max_length=52, null=True, verbose_name='URL slug'),
        ),
    ]