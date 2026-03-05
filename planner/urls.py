from django.urls import path
from .views import GoalListCreateView, GoalDetailView, TaskListCreateView, TaskDetailView

urlpatterns = [
    path('goals/', GoalListCreateView.as_view()),
    path('goals/<int:pk>/', GoalListCreateView.as_view()),

    path('tasks/', TaskListCreateView.as_view()),
    path('tasks/<int:pk>/', TaskDetailView.as_view()),
]