from django.db import models

# Create your models here.
# 分类
class Category(models.Model):
    name = models.CharField('名称', max_length=30)
    class Meta:
        verbose_name = '类别'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

# 标签
class Tag(models.Model):
    name = models.CharField('名称', max_length=20)

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 博客
class Blog(models.Model):
    title = models.CharField('标题', max_length=250)
    author = models.CharField('作者', max_length=20)
    content = models.TextField('内容')
    pub_date = models.DateTimeField('发布时间', auto_now_add=True)
    view_num = models.PositiveIntegerField('阅读量', default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='分类')
    tag = models.ManyToManyField(Tag, verbose_name='标签')

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = '博客'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

# 评论
class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, verbose_name='博客')
    name = models.CharField('姓名', max_length=20)
    email = models.EmailField('邮箱')
    content = models.CharField('内容', max_length=250)
    pub_date = models.DateTimeField('发布时间', auto_now_add=True)

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

