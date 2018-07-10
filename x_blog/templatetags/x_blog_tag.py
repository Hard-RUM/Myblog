from django import template
from django.db.models import Count
from ..models import Post, Category,Tag

register = template.Library()


# 指定最新文章部分显示个数为3,装饰器
@register.simple_tag
def get_recent_posts_list(num=5):
    return Post.objects.all().order_by('-created_time')[:num]


# 文章归档
@register.simple_tag
def archives(num=5):
    return Post.objects.dates('created_time', 'month', order='DESC')[:num]


# 文章的分类
@register.simple_tag
def classification():
    return Category.objects.all()

#云标签
@register.simple_tag
def get_tags():
    return Tag.objects.annotate(num_post=Count('post')).filter(num_post__gt=0)