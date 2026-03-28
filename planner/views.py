# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import User
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.serializers import ModelSerializer
from .models import Goal, Task, Category
from .serializers import GoalSerializer, TaskSerializer, CategorySerializer

class RegisterSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

class GoalListCreateView(generics.ListCreateAPIView):
    serializer_class = GoalSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [OrderingFilter, SearchFilter]
    ordering_fields = ['id', 'title']
    ordering = ['-id']
    search_fields = ['title', 'description']
    def get_queryset(self):
        return Goal.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class GoalDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GoalSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Goal.objects.filter(user=self.request.user)

class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ['goal', 'completed']
    ordering_fields = ['id', 'title', 'completed']
    ordering = ['-id']
    search_fields = ['title', 'description']

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

class CategoryListView(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Category.objects.all()
