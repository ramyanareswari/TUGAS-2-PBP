from urllib import response
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, HttpResponseForbidden
from django.urls import reverse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from todolist.forms import CreateNew
from todolist.models import Task
from django.core import serializers

# ============================/ASSIGNMENT 4/============================

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    task_list = Task.objects.all()
    task_data=[]
    user = request.user

    for task in task_list:
        if task.user == user:
            task_data.append(task)
    context = {
        'task_data':task_data,
        'name' : request.user,
    }
    return render(request, 'todolist.html', context)

@login_required(login_url='/todolist/login/')
def create_task(request):
    # Memanggil CreateNew dari forms.py
    task_form = CreateNew(request.POST)
    if request.method == 'POST':
        
            task_form = CreateNew(request.POST)
            if task_form.is_valid():
                new = task_form.save(commit=False)
                # Set the current logged in user
                task_form.instance.user = request.user
                new.save()

                response=HttpResponseRedirect(reverse("todolist:show_todolist"))
                return response

    context = {'task_form' : task_form}
    return render(request, 'create_task.html', context)

# ============================/ASSIGNMENT 6/============================

@login_required(login_url='/todolist/login/')
def show_todolist_new(request):
    task_list = Task.objects.all()
    task_data=[]
    user = request.user

    for task in task_list:
        if task.user == user:
            task_data.append(task)
    context = {
        'task_data':task_data,
        'name' : request.user,
    }
    return render(request, 'todolist_new.html', context)

#  A view which returns a JSON object from json database
def get_task_json(request):
    task_item = Task.objects.all()
    return HttpResponse(serializers.serialize('json', task_item), content_type="application/json")

# A view to add task
@login_required(login_url='/auth/login/')
def add(request):
    form = CreateNew(request.POST)
    if (form.is_valid() and request.method == 'POST'):
        user = request.user
        title = request.POST.get('title')
        description = request.POST.get('description')
        task = Task(user=user, title=title, description=description)

        # Save submitted form data to model
        task.save()

        return JsonResponse({"fields": {
            "is_finished": task.is_finished,
            "title": title,
            "description": description,
            "date": task.date,
        }})        


# =================================/AUTH/=======================================

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

def delete_task(request, id):
    task_delete= Task.objects.filter(pk=id)
    task_delete.delete()
    return redirect(reverse("todolist:show_todolist"))

def update_task(request, id):
    task_update= Task.objects.get(pk=id)
    task_update.is_finished = not task_update.is_finished
    task_update.save()
    return redirect(reverse("todolist:show_todolist"))