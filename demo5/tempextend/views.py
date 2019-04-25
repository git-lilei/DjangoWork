from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from .form import CustomForm
# Create your views here.
def list(request):
    return render(request, 'tempextend/list.html')

def login(request):
    if request.method == 'GET':
        form = CustomForm()
        return render(request, 'tempextend/login.html', {'form': form})

    elif request.method == 'POST':
        form = CustomForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            form.save()
            print(username, password)
            return redirect(reverse('tempextend:list'))