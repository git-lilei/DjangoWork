from django.contrib.syndication.views import Feed
from .models import Blog
from django.shortcuts import reverse

class BlogFeed(Feed):
    title = '文章'
    description = '内容'
    link = '/'

    def items(self):
        return Blog.objects.all()

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content

    def item_link(self, item):
        return reverse('blogs:blogdetail', args=[item.id])