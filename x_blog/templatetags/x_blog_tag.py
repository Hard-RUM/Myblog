from django import template

from ..models import Post, Category

register = template.Library()


# 指定最新文章部分显示个数为3,装饰器
@register.simple_tag
def get_recent_posts_list(num=3):
    return Post.objects.all().order_by('-created_time')[:num]


# 文章归档
@register.simple_tag
def archives(num=5):
    return Post.objects.dates('created_time', 'month', order='DESC')[:num]


# 文章的分类
@register.simple_tag
def classification():
    return Category.objects.all()
