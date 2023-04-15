from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView
from .models import Task


# Define a class-based view called TaskList that inherits from Django's built-in ListView class
class TaskList(ListView):
    model = Task
    # overriding the default name of object_list
    context_object_name = 'tasks'


def task_detail(request, task_id):
    task_detail = Task.objects.get(id=task_id)
    context_dictionary = {'task_detail': task_detail}
    return render(request, 'task_detail.html', context_dictionary)


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')


def logout_user(request):
    logout(request)
    return redirect('home')