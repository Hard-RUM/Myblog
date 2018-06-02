from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '博客类别'
        verbose_name = '博客类别'


class Tag(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '博客标签'
        verbose_name = '博客标签'


class Post(models.Model):
    # 帖子标题，内容
    title = models.CharField(max_length=200, verbose_name='博客主标题')
    subtitle_title = models.CharField(max_length=100, verbose_name='single里的副标题')
    img = models.ImageField(upload_to='media', verbose_name='blog/single通用界面图片')
    # thumbnail = models.ImageField(upload_to='avatar/%Y/%m/%d/', default='default.jpg', verbose_name='头像')
    content_1 = models.TextField(null=True, verbose_name='博客内容：第一段')
    content_2 = models.TextField(null=True, verbose_name='博客内容：第二段')
    # 摘要
    excerpt = models.CharField(max_length=200, blank=True, null=True, verbose_name='博客简介')

    # 创建时间,自动加上发布时间
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    # 定义关联关系,一对多的关系,一个类别对应多个帖子
    category = models.ForeignKey('Category', verbose_name='博客类别')
    tag = models.ManyToManyField('Tag', blank=True, verbose_name='博客标签')
    # author = models.ForeignKey(User, verbose_name='帖子作者')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        #返回这个字符串：/post/1/
        return reverse('x_blog:single',kwargs={'pk': self.pk})

    class Meta:
        verbose_name_plural = '博客页管理'
        verbose_name = '博客页管理'
