from django.shortcuts import render

# Create your views here.
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Goal,Task
from .serializers import GoalSerializer, TaskSerializer

class GoalListCreateView(generics.ListCreateAPIView):
    serializer_class = GoalSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Goal.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class GoalDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GoalSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Goal.objects.filter(goal__user=self.request.user)

class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    # This method defines what data will be returned in GET request
    # This method filters tasks so user sees only their own tasks
    def get_queryset(self):
        # We access current user via self.request.user
        # Then we filter tasks through relationship:
        # Task → Goal → User
        return Task.objects.filter(goal__user=self.request.user)
    def perform_create(self, serializer):
        serializer.save()

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Task.objects.filter(goal__user=self.request.user)

