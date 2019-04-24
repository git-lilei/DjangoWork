from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import markdown
from .models import *


# Create your views here.
# 首页
def index(request):
    blogs = Blog.objects.all()

    paginator = Paginator(blogs, 2)
    page = request.GET.get('page')
    try:
        bloglist = paginator.page(page)
    except PageNotAnInteger:
        bloglist = paginator.page(1)
    except EmptyPage:
        bloglist = paginator.page(paginator.num_pages)

    bloglist3 = Blog.objects.all()[:3]
    categorylist = Category.objects.all()
    taglist = Tag.objects.all()[:10]
    dates = Blog.objects.dates('pub_date', 'month', order='DESC')[:3]
    return render(request, 'blog/index.html', {'bloglist': bloglist, 'bloglist3': bloglist3,
                                               'categorylist': categorylist, 'taglist': taglist, 'dates': dates})


# 归档
def archives(request, year, month):
    bloglist = Blog.objects.filter(pub_date__year=year, pub_date__month=month)
    bloglist3 = Blog.objects.all()[:3]
    categorylist = Category.objects.all()
    taglist = Tag.objects.all()[:10]
    dates = Blog.objects.dates('pub_date', 'month', order='DESC')[:3]
    return render(request, 'blog/index.html', {'bloglist': bloglist, 'bloglist3': bloglist3,
                                               'categorylist': categorylist, 'taglist': taglist, 'dates': dates})


# 标签
def tag(request, tid):
    bloglist = get_object_or_404(Tag, pk=tid).blog_set.all()
    bloglist3 = Blog.objects.all()[:3]
    categorylist = Category.objects.all()
    taglist = Tag.objects.all()[:10]
    dates = Blog.objects.dates('pub_date', 'month', order='DESC')[:3]
    return render(request, 'blog/index.html', {'bloglist': bloglist, 'bloglist3': bloglist3,
                                               'categorylist': categorylist, 'taglist': taglist, 'dates': dates})


# 分类
def category(request, cid):
    cate = get_object_or_404(Category, pk=cid)
    bloglist = Blog.objects.filter(category=cate)
    bloglist3 = Blog.objects.all()[:3]
    categorylist = Category.objects.all()
    taglist = Tag.objects.all()[:10]
    dates = Blog.objects.dates('pub_date', 'month', order='DESC')[:3]
    return render(request, 'blog/index.html', {'bloglist': bloglist, 'bloglist3': bloglist3,
                                               'categorylist': categorylist, 'taglist': taglist, 'dates': dates})


# 详情页
def blogdetail(request, bid):
    blogdetail = Blog.objects.get(pk=bid)
    blogdetail.view_num += 1
    blogdetail.save()
    blogdetail.content = markdown.markdown(blogdetail.content,
                                           extensions=[
                                               'markdown.extensions.extra',
                                               'markdown.extensions.codehilite',
                                               'markdown.extensions.toc',
                                           ])
    commentlist = blogdetail.comment_set.all()
    bloglist = Blog.objects.all()
    bloglist3 = Blog.objects.all()[:3]
    categorylist = Category.objects.all()
    taglist = Tag.objects.all()[:10]
    dates = Blog.objects.dates('pub_date', 'month', order='DESC')[:3]
    return render(request, 'blog/single.html', {'blogdetail': blogdetail, 'commentlist': commentlist,
                                                'bloglist': bloglist, 'bloglist3': bloglist3,
                                                'categorylist': categorylist, 'taglist': taglist, 'dates': dates})


# 添加评论
def addcomment(request, bid):
    name = request.POST['name']
    email = request.POST['email']
    comment = request.POST['comment']
    blog = Blog.objects.get(pk=bid)
    Comment.objects.create(name=name, email=email, content=comment, blog=blog)
    return redirect(reverse('blog:blogdetail', args=[str(bid)]))
