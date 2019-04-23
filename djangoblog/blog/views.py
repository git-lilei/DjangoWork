from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse


# Create your views here.
# 首页
def index(request):
    return render(request, 'blog/index.html')
