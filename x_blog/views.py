from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# Create your views here.
from .models import Post, Category
import markdown


def index(request):
    # return HttpResponse('Text OK')
    return render(request, 'x_blog/index.html', locals())


def blog(request):
    # 后台返回个文章列表
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'x_blog/blog.html', locals())


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
    return render(request, 'x_blog/single.html', locals())


def archives(request, year, month):
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month).order_by("-created_time")
    return render(request, 'x_blog/blog.html', locals())


def categories(request,pk):
    category = get_object_or_404(Category, pk=pk)
    post_list = category.post_set.all()
    return render(request, 'x_blog/blog.html', {'post_list': post_list})