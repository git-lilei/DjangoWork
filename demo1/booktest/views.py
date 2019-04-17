from django.shortcuts import render
from django.http import HttpResponse
from .models import BookInfo
from django.template import loader


# Create your views here.

def index(request):
    # return HttpResponse('首页')
    # 加载模板
    # template = loader.get_template('booktest/index.html')
    # context = {'username': 'MrBean'}
    # result = template.render(context=context)
    # return HttpResponse(result)

    return render(request, 'booktest/index.html', {'username': 'MrBean'})


def list(request):
    # return HttpResponse('列表页')
    # template = loader.get_template('booktest/list.html')
    # booklist = BookInfo.objects.all()
    # context = {"booklist": booklist}
    # result = template.render(context=context)
    # return HttpResponse(result)

    booklist = BookInfo.objects.all()
    return render(request, 'booktest/list.html', {"booklist": booklist})


def detail(request, id):
    try:
        # template = loader.get_template('booktest/detail.html')
        # book = BookInfo.objects.get(pk=int(id))
        # context = {'book':book}
        # result = template.render(context=context)
        # return HttpResponse(result)

        book = BookInfo.objects.get(pk=int(id))
        return render(request, 'booktest/detail.html', {'book': book})
    except:
        return HttpResponse('未知错误')
