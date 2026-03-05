from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Goal,Task
from .serializers import GoalSerializer, TaskSerializer

class GoalListCreateView(generics.ListCreateAPIView):
    def get_queryset(self):
        return Goal.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    serializer_class = GoalSerializer

class TaskListCreateView(generics.ListCreateAPIView):
    # This method defines what data will be returned in GET request
    # This method filters tasks so user sees only their own tasks
    def get_queryset(self):
        # We access current user via self.request.user
        # Then we filter tasks through relationship:
        # Task → Goal → User
        return Task.objects.filter(goal__user=self.request.user)
    serializer_class = TaskSerializer





