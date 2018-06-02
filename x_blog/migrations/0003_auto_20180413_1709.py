# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-04-13 09:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('x_blog', '0002_auto_20180317_2338'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': '博客类别', 'verbose_name_plural': '博客类别'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': '博客页管理', 'verbose_name_plural': '博客页管理'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': '博客标签', 'verbose_name_plural': '博客标签'},
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.RemoveField(
            model_name='post',
            name='modified_time',
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='x_blog.Category', verbose_name='博客类别'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(verbose_name='博客内容'),
        ),
        migrations.AlterField(
            model_name='post',
            name='excerpt',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='博客简介'),
        ),
        migrations.AlterField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(blank=True, to='x_blog.Tag', verbose_name='博客标签'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=200, verbose_name='博客标题'),
        ),
    ]
