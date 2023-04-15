from django.contrib import admin
from .models import Task

# registering database models
admin.site.register(Task)
