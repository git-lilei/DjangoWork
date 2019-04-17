from django.contrib import admin
from .models import BookInfo, HeroInfo


# Register your models here.
class HeroInfoInline(admin.StackedInline):
    model = HeroInfo
    extra = 1


class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['title', 'pub_date']
    list_filter = ['btitle']
    search_fields = ['btitle']
    list_per_page = 2

    inlines = [HeroInfoInline]


class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'gender', 'content']
    list_filter = ['hname', 'hgender']
    search_fields = ['hname', 'hcontent']
    list_per_page = 2


admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo, HeroInfoAdmin)
