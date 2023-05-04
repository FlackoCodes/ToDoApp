from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .views import TaskList, EditTask


urlpatterns = [
    path('', TaskList.as_view(), name='task-list'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('task/<int:task_id>', views.task_detail, name='task-detail'),
    path('create-task/', views.create_task, name='create-task'),
    path('delete-task/<int:task_id>', views.delete_task, name='delete-task'),
    path('edit-task/<int:task_id>', EditTask.as_view(), name='edit-task'),
    path('create-account/', views.create_account, name='sign-up'),
    path('search/', views.search, name='search'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)