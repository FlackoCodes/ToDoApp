from django.urls import path
from . import views
from .views import TaskList

urlpatterns = [
    path('', TaskList.as_view(), name='task-list'),
    path('task/<int:task_id>', views.task_detail, name='task-detail'),
]