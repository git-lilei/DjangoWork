from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import StudentInfo,ClassInfo
# Create your views here.
def index(request):
    # return HttpResponse('index')
    context = {'username': 'MrBean'}
    return render(request,'studenttest/index.html',context)

def list(request):
    # return HttpResponse('list')
    classlist = ClassInfo.objects.all()
    context = {'classlist': classlist}
    return render(request,'studenttest/list.html',context)

def detail(request,id):
    # return HttpResponse('detail')
    classinfo = ClassInfo.objects.get(pk=id)
    context = {'classinfo': classinfo}
    return render(request,'studenttest/detail.html', context)