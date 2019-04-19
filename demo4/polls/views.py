from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choose


# Create your views here.
def index(request):
    return render(request, 'polls/index.html', {'username': 'MrBean'})


def list(request):
    qlist = Question.objects.all()
    return render(request, 'polls/list.html', {'qlist': qlist})


def detail(request, id):
    try:
        question = Question.objects.get(pk=id)
        return render(request, 'polls/detail.html', {'question': question})
    except:
        return HttpResponse('未知错误')


def vote(request, cid):
    try:

        choose = Choose.objects.get(pk=cid)
        choose.cvote += 1
        choose.save()
        qid = choose.cquestion.id
        print(type(qid))
        return HttpResponseRedirect('/polls/detail/'+str(qid)+'/')
    except:
        return HttpResponse('未知错误')
