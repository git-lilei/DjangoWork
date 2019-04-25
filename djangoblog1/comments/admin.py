from django.contrib import admin
from .models import *


# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    list_display = ['blog', 'name', 'content', 'pub_date', ]


admin.site.register(Comment, CommentAdmin)
