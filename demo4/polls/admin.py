from django.contrib import admin
from .models import Question, Choose


# Register your models here.
class ChooseInline(admin.StackedInline):
    model = Choose
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'qn', 'pub_date']
    list_filter = ['qname']
    search_fields = ['qname']
    list_per_page = 2

    inlines = [ChooseInline]


class ChooseAdmin(admin.ModelAdmin):
    list_display = ['id', 'cn', 'vote']
    list_filter = ['cname']
    search_fields = ['cname']
    list_per_page = 2


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choose, ChooseAdmin)
