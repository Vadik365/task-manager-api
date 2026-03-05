from django.shortcuts import render

# Create your views here.
from rest_framework.exceptions import PermissionDenied
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
    def perform_create(self, serializer):
        # Get Goal object from validated data
        goal = serializer.validated_data["goal"]
        #Security chek: goal must belong to cuurent user
        if goal.user != self.request.user:
            raise PermissionDenied("You cannot create tasks for other users")
        #Save task if everything is Ok
        serializer.save()
    serializer_class = TaskSerializer

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    def get_queryset(self):
        return Task.objects.filter(goal__user=self.request.user)

class GoalDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GoalSerializer
    def get_queryset(self):
        return Goal.objects.filter(goal__user=self.request.user)


