# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-04-14 08:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('x_blog', '0005_auto_20180414_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(upload_to='media', verbose_name='图片'),
        ),
    ]
