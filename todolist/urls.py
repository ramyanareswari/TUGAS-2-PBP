# Implementasi routing terhadap views.py
from django.urls import path
from todolist.views import delete_task, get_task_json, show_todolist, show_todolist_new,create_task, register, login_user, logout_user, delete_task, update_task, add

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('new/', show_todolist_new, name="show_todolist_new"),

    path('add/', add, name="add"),
    path('json/', get_task_json, name="get_task_json"),

    path('create-task/', create_task, name='create_task'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('delete-task/<int:id>', delete_task, name='delete-task'),
    path('update-task/<int:id>', update_task, name='update-task'),
] 