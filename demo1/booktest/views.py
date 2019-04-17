from django.shortcuts import render
from django.http import HttpResponse
from .models import BookInfo


# Create your views here.

def index(request):
    return HttpResponse('首页')


def list(request):
    return HttpResponse('列表页')


def detail(request, id):
    try:
        book = BookInfo.objects.get(pk=int(id))
        return HttpResponse(book)
    except:
        return HttpResponse('未知错误')
