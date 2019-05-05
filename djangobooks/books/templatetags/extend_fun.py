from django import template
from ..models import *
register = template.Library()


@register.simple_tag
def gethotpics():
    '''
    获取热图
    '''
    return HotPic.objects.all()


