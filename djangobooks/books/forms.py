from django.forms import ModelForm
from .models import User


class UserForm(ModelForm):
    '''
    评论模型对应的表单类
    '''

    class Meta():
        model = User
        fields = ['name', 'pwd', 'college', 'num', 'email']