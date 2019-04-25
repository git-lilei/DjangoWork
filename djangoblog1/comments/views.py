from django.shortcuts import render, reverse, redirect, get_object_or_404
from .forms import CommentForm
from django.http import HttpResponse
from blogs.models import Blog
# Create your views here.


# 添加评论
def addcomment(request, bid):
    blog = get_object_or_404(Blog, pk=bid)
    if request.method == 'POST':
        comment = CommentForm(request.POST)
        if comment.is_valid():
            comment = comment.save(commit=False)
            comment.blog = blog
            comment.save()
            return redirect(reverse('blogs:blogdetail', args=[str(bid)]))
        else:
            return HttpResponse('评论失败')
    else:
        return HttpResponse('评论失败')
