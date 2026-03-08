from rest_framework import serializers
from .models import Goal, Task


class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = '__all__'
        read_only_fields = ['user']

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
    def validate_goal(self, value):
        request = self.context.get('request')

        if request in value.user != request.user:
            raise serializers.ValidationError(detail="You cannot use another user's goal.")
        return value