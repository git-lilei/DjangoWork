from django.db import models
from blogs.models import Blog


# Create your models here.
# 评论
class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, verbose_name='博客')
    name = models.CharField('姓名', max_length=20)
    email = models.EmailField('邮箱')
    content = models.TextField('内容', max_length=250)
    pub_date = models.DateTimeField('发布时间', auto_now_add=True)

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
