# Implementasi routing terhadap views.py
from django.urls import path
from todolist.views import delete_task, show_todolist, create_task, register, login_user, logout_user, delete_task, update_task

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('create-task/', create_task, name='create_task'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('delete-task/<int:id>', delete_task, name='delete-task'),
    path('update-task/<int:id>', update_task, name='update-task'),
] 