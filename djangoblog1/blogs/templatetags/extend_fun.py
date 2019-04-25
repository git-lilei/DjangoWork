from django import template
from ..models import Blog, Category, Tag

register = template.Library()


@register.simple_tag
def getnewblogs(num=3):
    '''
    获取最新文章，默认显示3篇
    :param num:
    :return:
    '''
    return Blog.objects.all()[:num]


@register.simple_tag
def getdatelist(num=3):
    '''
    返回最近月份
    :param num:
    :return:
    '''
    return Blog.objects.dates('pub_date', 'month', order='DESC')[:num]


@register.simple_tag
def getcategorys():
    '''
    返回分类
    :return:
    '''
    return Category.objects.all()


@register.simple_tag
def gettags():
    '''
    返回标签云
    :return:
    '''
    return Tag.objects.all()[:10]
