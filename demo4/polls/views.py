from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choose


# Create your views here.
# 首页
def index(request):
    return render(request, 'polls/index.html', {'username': 'MrBean'})


# 列表
def list(request):
    qlist = Question.objects.all()
    return render(request, 'polls/list.html', {'qlist': qlist})


# 投票详情页
def detail(request, id):
    try:
        question = Question.objects.get(pk=id)
        return render(request, 'polls/detail.html', {'question': question})
    except:
        return HttpResponse('未知错误')


# 投票
def vote(request, cid):
    try:

        choose = Choose.objects.get(pk=cid)
        choose.cvote += 1
        choose.save()
        qid = choose.cquestion.id
        print(type(qid))
        return HttpResponseRedirect('/polls/detail/' + str(qid) + '/')
    except:
        return HttpResponse('未知错误')


# 添加投票问题
def addquestion(request):
    return render(request, 'polls/addquestion.html')


# 执行添加投票问题
def addquehandler(request):
    try:
        qname = request.POST['qname']
        Question.objects.create(qname=qname)
        return HttpResponseRedirect('/polls/list')
    except:
        return HttpResponse('未知错误~')


# 添加问题选项
def addchoose(request, qid):
    return render(request, 'polls/addchoose.html', {'qid': qid})


# 执行添加问题选项
def addchoosehandler(request):
    try:
        cname = request.POST['cname']
        qid = request.POST['qid']
        question = Question.objects.get(pk=qid)
        Choose.objects.create(cname=cname, cquestion=question)
        return HttpResponseRedirect('/polls/detail/' + str(qid) + '/')
    except:
        return HttpResponse('未知错误~')
