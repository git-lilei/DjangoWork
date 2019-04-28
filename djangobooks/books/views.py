from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import UserForm
import datetime
from datetime import timedelta


# Create your views here.
# 首页
def index(request):
    return render(request, 'books/index.html')


# 主页
def reader(request):
    uid = User.objects.get(name = request.session.get('username')).id
    user = User.objects.get(pk=uid)
    return render(request, 'books/reader.html', {'user': user})


# 用户登录
def login(request):
    if request.method == 'GET':
        return render(request, 'books/reader_login.html')
    elif request.method == 'POST':
        name = request.POST['username']
        pwd = request.POST['password']
        res = User.objects.filter(name=name).first()
        if res:
            if res.pwd == pwd:
                request.session['username'] = name
                return render(request, 'books/reader.html', {'user': res})
            else:
                return render(request, 'books/reader_login.html', {'error': '密码信息错误'})
        else:
            return render(request, 'books/reader_login.html', {'error': '账号信息错误'})


# 用户注册
def register(request):
    if request.method == 'GET':
        user = UserForm(request.POST)
        return render(request, 'books/register.html', {'user': user})
    elif request.method == 'POST':
        user = UserForm(request.POST)
        if user.is_valid():
            user.save()
            return redirect(reverse('books:login'))
        else:
            return render(request, 'books/register.html', {'error': '注册失败', 'user': user})


# 注销登录
def loginout(request):
    del request.session['username']
    return redirect(reverse('books:index'))


# 查看个人信息
def userdetail(request, uid):
    user = get_object_or_404(User, pk=uid)
    return render(request, 'books/reader_info.html', {'user': user})


# 修改个人信息
def updateUserInfo(request, uid):
    if request.method == 'GET':
        user = UserForm(request.POST)
        return render(request, 'books/reader_modify.html', {'uid': uid, 'user': user})
    elif request.method == 'POST':
        userinfo = get_object_or_404(User, pk=uid)
        user = UserForm(request.POST, instance=userinfo)
        if user.is_valid():
            user.save()
            return render(request, 'books/reader_info.html', {'user': userinfo})
        else:
            return render(request, 'books/reader_modify.html', {'error': '修改失败', 'uid': uid, 'user': userinfo})


# 进入查询的页面
def checkall(request):
    return render(request, 'search/search.html')


# 查看书籍信息
def readerbook(request, bid):
    if request.method == 'GET':
        book = get_object_or_404(Book, pk=bid)
        reader = History.objects.filter(book=book).first()
        return render(request, 'books/reader_book.html', {'book': book, 'reader': reader})
    elif request.method == 'POST':
        book = get_object_or_404(Book, pk=bid)
        reader = History.objects.filter(book=book).first()
        if reader:
            return render(request, 'books/reader_book.html', {'book': book, 'reader': reader, 'error': '该书已经被借阅'})
        else:
            h = History()
            h.book = book
            h.user = User.objects.get(name=request.session.get("username"))

            h.return_date = datetime.datetime.now() + timedelta(days=30)
            h.save()
            reader = History.objects.filter(book=book).first()
            return render(request, 'books/reader_book.html', {'book': book, 'reader': reader})


# 查看阅读记录
def userhistory(request, uid):
    user = get_object_or_404(User, pk=uid)
    historys = History.objects.filter(user=user)
    if historys:
        return render(request, 'books/reader_histroy.html', {'historys': historys})
    else:
        return render(request, 'books/reader_histroy.html', {'error': '还没有借阅信息'})
