from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# Create your views here.
from .models import Post, Category
from django.views.generic import ListView
from utils import custom_paginator
import markdown


def index(request):
    # return HttpResponse('Text OK')

    return render(request, 'index.html', locals())


def blog(request):
    # 后台返回个文章列表
    post_list = Post.objects.all().order_by('-created_time')

    return render(request, 'x_blog/blog.html', locals())


class BlogView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'post_list'
    # 开始分页功能，每页放3条数据
    paginate_by = 3

    # 重写get_context_data,放入分页的起始页面和结束页码
    def get_context_data(self, **kwargs):
        # 调用父类的get_context_data方法
        context = super().get_context_data(**kwargs)
        # 获取分页相关的变量
        page = context.get('page_obj')
        paginator = context.get('paginator')

        # 调用自定义的分页方法
        start, end = custom_paginator(page.number, paginator.num_pages, 5)
        # 将start和end写入context中
        context.update({
            'page_range': range(start, end + 1)
        })
        # 返回context
        return context


def photos(request):
    # post=Post.objects.get(pk=pk)
    return render(request, 'x_blog/photos.html', locals())


def short_codes(request):
    return render(request, 'x_blog/short_codes.html', locals())


def mail(request):
    return render(request, 'x_blog/mail.html', locals())


def single(request, pk):
    post = Post.objects.get(pk=pk)
    # 后台返回个文章列表
    post.content_2 = markdown.markdown(post.content_2,
                                       extensions=[
                                           'markdown.extensions.extra',
                                           'markdown.extensions.codehilite',
                                           'markdown.extensions.toc'
                                       ])
    post_list = Post.objects.all().order_by('-created_time')
    post.increase_views()
    return render(request, 'x_blog/single.html', locals())


def archives(request, year, month):
    post = Post.objects.get(request)
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month).order_by("-created_time")
    post.increase_like()
    return render(request, 'x_blog/blog.html', locals())


# def detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#
#     post.increase_views()
#     return render(request, 'x_blog/blog.html', locals())


def categories(request, pk):
    category = get_object_or_404(Category, pk=pk)
    post_list = category.post_set.all()

    return render(request, 'x_blog/blog.html', {'post_list': post_list})
