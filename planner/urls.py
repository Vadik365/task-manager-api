from django.urls import path
from .views import GoalListCreateView, TaskListCreateView

urlpatterns = [
    path('goals/', GoalListCreateView.as_view()),
    path('tasks/', TaskListCreateView.as_view()),
]