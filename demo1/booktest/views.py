from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import BookInfo, HeroInfo
from django.template import loader


# Create your views here.
# 首页
def index(request):
    return render(request, 'booktest/index.html', {'username': request.session.get('username')})


# 登录
def login(request):
    if request.method == 'GET':
        return render(request, 'booktest/login.html')
    elif request.method == 'POST':
        request.session['username'] = request.POST['username']
        return redirect(reverse('booktest:booktest'))


# 退出登录
def loginout(request):
    request.session.clear()
    return redirect(reverse('booktest:booktest'))

# 图书列表
def list(request):
    booklist = BookInfo.objects.all()
    return render(request, 'booktest/list.html', {"booklist": booklist})


# 角色详情页
def detail(request, id):
    try:
        book = BookInfo.objects.get(pk=int(id))
        return render(request, 'booktest/detail.html', {'book': book})
    except:
        return HttpResponse('未知错误')


# 添加图书
def addbook(request):
    return render(request, 'booktest/addbook.html')


# 执行添加图书
def addbookhandler(request):
    btitleinfo = request.POST['btitle']
    BookInfo.objects.create(btitle=btitleinfo)
    return HttpResponseRedirect('/booktest/list')


# 添加角色
def addhero(request, bookid):
    return render(request, 'booktest/addhero.html', {"bookid": bookid})


# 处理添加角色
def addherohandler(request):
    bookid = request.POST['bookid']
    hname = request.POST['hname']
    hgender = request.POST['hgender']
    hcontent = request.POST['hcontent']
    book = BookInfo.objects.get(pk=bookid)
    h = HeroInfo()
    h.hname = hname
    if hgender == '1':
        h.hgender = True
    else:
        h.hgender = False
    h.hcontent = hcontent
    h.hbook = book
    h.save()
    return HttpResponseRedirect('/booktest/detail/' + str(bookid) + '/')


# 删除图书
def delete(request, id):
    try:
        BookInfo.objects.get(pk=int(id)).delete()
        return HttpResponseRedirect('/booktest/list/')
    except:
        return HttpResponse('未知错误')


# 删除角色
def deletehero(request, id):
    try:
        hero = HeroInfo.objects.get(pk=int(id))
        hero.delete()
        bookid = hero.hbook.id
        return HttpResponseRedirect('/booktest/detail/' + str(bookid) + '/')
    except:
        return HttpResponse('未知错误')


# 修改图书
def updatebook(request, bookid):
    try:
        book = BookInfo.objects.get(pk=bookid)
        return render(request, 'booktest/updatebook.html', {'book': book})
    except:
        return HttpResponse('未知错误')


# 执行修改图书
def updatebookhandler(request, bookid):
    try:
        btitle = request.POST['btitle']
        book = BookInfo.objects.get(pk=bookid)
        book.btitle = btitle
        book.save()
        return HttpResponseRedirect('/booktest/list')
    except:
        return HttpResponse('未知错误')


# 修改角色
def updatehero(request, heroid):
    try:
        hero = HeroInfo.objects.get(pk=heroid)
        return render(request, 'booktest/updatehero.html', {'hero': hero})
    except:
        return HttpResponse('未知错误.')


# 执行修改角色
def updateherohandler(request, heroid):
    try:
        bookid = request.POST['bookid']
        hname = request.POST['hname']
        hgender = request.POST['hgender']
        hcontent = request.POST['hcontent']
        h = HeroInfo.objects.get(pk=heroid)
        h.hname = hname
        if hgender == '1':
            h.hgender = True
        else:
            h.hgender = False
        h.hcontent = hcontent
        h.save()
        return HttpResponseRedirect('/booktest/detail/' + str(bookid) + '/')
    except:
        return HttpResponse('未知错误')
