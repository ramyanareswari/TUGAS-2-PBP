from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from todolist.forms import CreateNew
from todolist.models import Task

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    task_data = Task.objects.filter(user=request.user)

    context = {
        'task_data':task_data,
        'name' : request.user,
    }
    return render(request, 'todolist.html', context)

@login_required(login_url='/todolist/login/')
def create_task(request):
    form = CreateNew(request.POST)
    if request.method == 'POST':
        
            form = CreateNew(request.POST)
            if form.is_valid():
                new = form.save(commit=False)
                new.user = request.user
                new.save()

                return redirect("todolist:show_todolist")

    context = {'form' : form}
    return render(request, 'create_task.html', context)

def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response