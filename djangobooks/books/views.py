from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import UserForm
import datetime
from datetime import timedelta
from django.core.mail import send_mail, send_mass_mail, EmailMultiAlternatives
from django.conf import settings
# 引入绘图模块
from PIL import Image, ImageDraw, ImageFont
import random, io
from django.views.decorators.cache import cache_page
from django.core.cache import cache

# Create your views here.
# 首页
# @cache_page(60*15)
def index(request):
    articles = Articles.objects.all()
    return render(request, 'books/index.html', {'articles': articles})

# 图表页面
def echarts(request):
    return render(request, 'books/echarts.html')

# 跳转到ajax页面
def ajax(request):
    return render(request, 'books/ajax.html')


# 请求ajax数据
def ajaxdata(request):
    if request.method == 'GET':
        return HttpResponse('GET请求成功')
    elif request.method == 'POST':
        return HttpResponse('POST请求成功')


# ajax登录
def ajaxlogin(request):
    if request.method == 'GET':
        return render(request, 'books/login.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        verifycode = request.POST["verifycode"]

        user = User.objects.filter(name=username, pwd=password).first()
        if user:
            if verifycode == request.session["verifycode"]:
                return HttpResponse("登录成功")
            else:
                return HttpResponse("验证码错误")
        else:
            return HttpResponse('登录失败')


# 检查用户
def checkuser(request):
    if request.method == 'POST':
        username = request.POST['username']
        user = User.objects.filter(name=username).first()
        if user:
            return HttpResponse('success')
        else:
            return HttpResponse('failed')


def verify(request):
    print('+++++++++')
    # 定义变量，用于画面的背景色、宽、高
    bgcolor = (random.randrange(20, 100),
               random.randrange(20, 100),
               random.randrange(20, 100))
    width = 100
    heigth = 25
    # 创建画面对象
    im = Image.new('RGB', (width, heigth), bgcolor)
    # 创建画笔对象
    draw = ImageDraw.Draw(im)
    # 调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, heigth))
    fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
    draw.point(xy, fill=fill)
    # 定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    # 随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    # 构造字体对象
    font = ImageFont.truetype('CABINSKETCH-BOLD.TTF', 23)
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    # 绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
    # 释放画笔
    del draw
    request.session['verifycode'] = rand_str
    f = io.BytesIO()
    im.save(f, 'png')
    # 将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(f.getvalue(), 'image/png')


# 发送邮件
def sendemail(request):
    try:
        # send_mail('django邮件', 'hello world！', settings.DEFAULT_FROM_EMAIL,
        #           ['1962695785@qq.com', '17630236231@163.com'])
        # send_mass_mail((('django邮件1', 'hello world！', settings.DEFAULT_FROM_EMAIL,
        #                  ['1962695785@qq.com', '17630236231@163.com']),
        #                 ('django邮件2', 'hello world！', settings.DEFAULT_FROM_EMAIL,
        #                  ['1962695785@qq.com', '17630236231@163.com'])
        #                 ))
        return HttpResponse('发送成功')
    except Exception as e:
        return HttpResponse('发送失败', e)


# 修改富文本
def addarticle(request):
    if request.method == 'GET':
        return render(request, 'books/addarticle.html')
    elif request.method == "POST":
        title = request.POST['title']
        message = request.POST['message']
        a = Articles(title=title, message=message)
        a.save()
        return redirect(reverse('books:index'))


# 上传图片
def upload(request):
    if request.method == 'GET':
        return render(request, 'books/uploadpic.html')
    elif request.method == 'POST':
        name = request.POST['name']
        pic = request.FILES['pic']
        index = request.POST['index']
        hp = HotPic(name=name, pic=pic, index=index)
        hp.save()
        return redirect(reverse('books:index'))


# 主页
def reader(request):
    uid = User.objects.get(name=request.session.get('username')).id
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
