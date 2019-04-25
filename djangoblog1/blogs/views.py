from comments.forms import CommentForm
from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import markdown
from .models import *


# Create your views here.
# 分页
def pageblogs(request, blogs):
    paginator = Paginator(blogs, 2)
    page = request.GET.get('page')
    try:
        bloglist = paginator.page(page)
    except PageNotAnInteger:
        bloglist = paginator.page(1)
    except EmptyPage:
        bloglist = paginator.page(paginator.num_pages)

    return bloglist


# 首页
def index(request):
    blogs = Blog.objects.all()
    bloglist = pageblogs(request, blogs)

    return render(request, 'blogs/index.html', {'bloglist': bloglist})


# 详情页
def blogdetail(request, bid):
    comment = CommentForm(request.POST)
    blogdetail = Blog.objects.get(pk=bid)
    blogdetail.view_num += 1
    blogdetail.save()
    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])
    blogdetail.content = md.convert(blogdetail.content)
    blogdetail.toc = md.toc

    return render(request, 'blogs/single.html', {'blogdetail': blogdetail, 'form': comment})


# 归档
def archives(request, year, month):
    blogs = Blog.objects.filter(pub_date__year=year, pub_date__month=month)
    bloglist = pageblogs(request, blogs)

    return render(request, 'blogs/index.html', {'bloglist': bloglist})


# 分类
def category(request, cid):
    blogs = get_object_or_404(Category, pk=cid).blog_set.all()
    bloglist = pageblogs(request, blogs)

    return render(request, 'blogs/index.html', {'bloglist': bloglist})


# 标签
def tag(request, tid):
    blogs = get_object_or_404(Tag, pk=tid).blog_set.all()
    bloglist = pageblogs(request, blogs)

    return render(request, 'blogs/index.html', {'bloglist': bloglist})
