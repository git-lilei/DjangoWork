from django.contrib import admin
from .models import *


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'pwd', 'college', 'num', 'email', ]


class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'author', 'pub_come', 'pub_date', ]


class HistoryAdmin(admin.ModelAdmin):
    list_display = ['book', 'user', 'borrow_date', 'return_date', 'status']


class HotPicAdmin(admin.ModelAdmin):
    list_display = ['name', 'pic', 'index']


class ArticlesAdmin(admin.ModelAdmin):
    list_display = ['title', 'message']


admin.site.register(User, UserAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(History, HistoryAdmin)
admin.site.register(HotPic, HotPicAdmin)
admin.site.register(Articles, ArticlesAdmin)
