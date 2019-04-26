from django.contrib import admin
from .models import *


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'pwd', 'college', 'num', 'email', ]


class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'author', 'pub_come', 'pub_date', ]


class HistoryAdmin(admin.ModelAdmin):
    list_display = ['book', 'user', 'borrow_date', 'return_date', 'status']


admin.site.register(User, UserAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(History, HistoryAdmin)
