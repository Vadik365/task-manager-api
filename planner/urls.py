from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import GoalListCreateView, GoalDetailView, TaskListCreateView, TaskDetailView, RegisterView, CategoryListView

urlpatterns = [
    path('register/', RegisterView.as_view(), name ='register'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('goals/', GoalListCreateView.as_view(), name ='goal-list-create'),
    path('goals/<int:pk>/', GoalDetailView.as_view(), name ='goal-detail'),

    path('tasks/', TaskListCreateView.as_view(), name ='task-list-create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name ='task-detail'),

    path('token/', TokenObtainPairView.as_view(), name ='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name ='token_refresh'),
]