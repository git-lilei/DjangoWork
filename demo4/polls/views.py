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


# 删除投票问题
def deletequestion(request, qid):
    try:
        Question.objects.get(pk=qid).delete()
        return HttpResponseRedirect('/polls/list')
    except:
        return HttpResponse('未知错误。')


# 删除投票选项
def deletechoose(request, cid):
    try:
        choose = Choose.objects.get(pk=cid)
        choose.delete()
        qid = choose.cquestion.id
        return HttpResponseRedirect('/polls/detail/' + str(qid) + '/')
    except:
        return HttpResponse('未知错误。')


# 修改投票问题
def updatequestion(request, qid):
    question = Question.objects.get(pk=qid)
    return render(request, 'polls/updatequestion.html', {'question': question})


# 执行修改投票问题
def updatequehandler(request, qid):
    try:
        qname = request.POST['qname']
        question = Question.objects.get(pk=qid)
        question.qname = qname
        question.save()
        return HttpResponseRedirect('/polls/list')
    except:
        return HttpResponse('未知错误~')


# 修改投票选项
def updatechoose(request, cid):
    try:
        choose = Choose.objects.get(pk=cid)
        return render(request, 'polls/updatechoose.html', {'choose': choose})
    except:
        return HttpResponse('未知错误。')


# 执行修改投票选项
def updatechoosehandler(request, cid):
    try:
        cname = request.POST['cname']
        cvote = request.POST['cvote']
        qid = request.POST['qid']
        choose = Choose.objects.get(pk=cid)
        choose.cname = cname
        if int(cvote) < 0:
            choose.cvote = cvote[1:]
        else:
            choose.cvote = cvote
        choose.save()
        return HttpResponseRedirect('/polls/detail/' + str(qid) + '/')
    except:
        return HttpResponse('未知错误')
