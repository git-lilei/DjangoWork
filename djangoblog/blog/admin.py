from django.contrib import admin
from .models import *


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', ]


class TagAdmin(admin.ModelAdmin):
    list_display = ['name', ]


class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'content', 'pub_date', 'view_num', ]


class CommentAdmin(admin.ModelAdmin):
    list_display = ['blog', 'name', 'content', 'pub_date', ]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)
