from rest_framework import serializers
from .models import Goal, Task, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class GoalSerializer(serializers.ModelSerializer):
    total_tasks = serializers.SerializerMethodField()
    completed_tasks = serializers.SerializerMethodField()

    class Meta:
        model = Goal
        fields = ['id', 'title', 'description', 'category', 'user', 'total_tasks', 'completed_tasks']
        read_only_fields = ['user']

    def get_total_tasks(self, obj):
        return obj.task_set.count()

    def get_completed_tasks(self, obj):
        return obj.task_set.filter(completed=True).count()

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'completed', 'goal']
    def validate_goal(self, value):
        request = self.context.get('request')

        if request and value.user != request.user:
            raise serializers.ValidationError(detail="You cannot use another user's goal.")
        return value