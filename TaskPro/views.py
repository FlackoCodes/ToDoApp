from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView
from .models import Task
from .forms import TaskForm, SignUpForm


from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Define a class-based view called TaskList that inherits from Django's built-in ListView class
class TaskList(LoginRequiredMixin, ListView):
    model = Task
    # overriding the default name of object_list
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add the count of incomplete tasks to the context
        context['incomplete_task_count'] = Task.objects.filter(complete=False).count()
        return context

@login_required(login_url='login')
def task_detail(request, task_id):
    task_details = Task.objects.get(id=task_id)
    context_dictionary = {'task_details': task_details}
    return render(request, 'task_detail.html', context_dictionary)



def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('task-list')
    return render(request, 'login.html')



def logout_user(request):
    logout(request)
    return redirect('task-list')


def create_task(request):
    form = TaskForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('task-list')
    context_dictionary = {'form':form}
    return render(request, 'create_task.html', context_dictionary)


class EditTask(UpdateView):
    model = Task
    fields = ['title', 'description', 'complete']
    template_name = 'update.html'
    success_url = reverse_lazy('task-list')
    pk_url_kwarg = 'task_id'


def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('task-list')


def create_account(request):
    if request.method == 'POST':
        # send everything in the post request to the signup form
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # authenticate and login newly created user
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('task-list')
    form = SignUpForm()
    context_dictionary = {'form':form}
    return render(request, 'register.html', context_dictionary)


def search(request):
    search_parameter = request.GET.get('q') if request.GET.get('q') is not None else ''
    tasks = Task.objects.filter(
        Q(title__icontains=search_parameter)

    )
    context = {'tasks': tasks, 'search_parameter': search_parameter}
    return render(request, 'TaskPro/task_list.html', context=context)
