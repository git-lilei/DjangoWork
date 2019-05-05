from django.db import models
from tinymce.models import HTMLField


# Create your models here.
# 用户表
class User(models.Model):
    name = models.CharField('姓名', max_length=20)
    pwd = models.CharField('密码', max_length=20)
    college = models.CharField('学院名', max_length=20)
    num = models.CharField('学号', max_length=20)
    email = models.EmailField('邮箱', blank=True, null=True)

    class Meta:
        verbose_name = '用户表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 图书表
class Book(models.Model):
    name = models.CharField('书名', max_length=50)
    author = models.CharField('作者', max_length=50)
    pub_come = models.CharField('出版社', max_length=50)
    pub_date = models.DateTimeField('出版日期')

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = '图书表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 借阅表
class History(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='图书')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
    borrow_date = models.DateTimeField('借书日期', auto_now_add=True)
    return_date = models.DateTimeField('归还日期')
    status = models.CharField('是否归还', default='否', max_length=20)

    class Meta:
        verbose_name = '借阅表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.status


# 首页热图
class HotPic(models.Model):
    name = models.CharField('图片名称', max_length=20)
    pic = models.ImageField('图片', upload_to='hotpic')
    index = models.SmallIntegerField('下标', unique=True)

    class Meta:
        verbose_name = '图片表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 富文本
class Articles(models.Model):
    title = models.CharField('文章标题', max_length=20)
    message = HTMLField('文章内容')

    class Meta:
        verbose_name = '文章表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
