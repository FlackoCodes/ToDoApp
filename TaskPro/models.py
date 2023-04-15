from django.db import models
from django.contrib.auth.models import User


# Setting up database columns.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.TextField(max_length=50)
    description = models.TextField()
    complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']

