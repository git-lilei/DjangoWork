from django.db import models


# Create your models here.
class Question(models.Model):
    qname = models.CharField(max_length=100)
    qpub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.qname

    def qn(self):
        return self.qname

    qn.short_description = '标题'

    def pub_date(self):
        return self.qpub_date

    pub_date.short_description = '发布日期'


class Choose(models.Model):
    cname = models.CharField(max_length=100)
    cvote = models.IntegerField(default=0)
    cquestion = models.ForeignKey('Question', on_delete=models.CASCADE)

    def __str__(self):
        return self.cname

    def cn(self):
        return self.cname

    cn.short_description = '投票内容'

    def vote(self):
        return self.cvote

    vote.short_description = '票数'
