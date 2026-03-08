from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Goal(models.Model):
        title = models.CharField(max_length=200)
        description = models.TextField(blank=True)
        category = models.ForeignKey(Category, on_delete=models.CASCADE)
        user = models.ForeignKey(User, on_delete=models.CASCADE)

        def __str__(self):
            return self.title

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    def __str__(self):
        return self.title