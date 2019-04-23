from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse
from .models import *

# Create your views here.
# 首页
def index(request):
    bloglist = Blog.objects.all()
    bloglist3 = Blog.objects.all()[:3]
    categorylist = Category.objects.all()
    taglist = Tag.objects.all()[:10]
    return render(request, 'blog/index.html', {'bloglist': bloglist, 'bloglist3': bloglist3,
                                               'categorylist': categorylist, 'taglist': taglist})
