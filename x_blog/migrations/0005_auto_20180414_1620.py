# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-04-14 08:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('x_blog', '0004_post_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(upload_to='media/%y/%m/%d', verbose_name='图片'),
        ),
    ]
