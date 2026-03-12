from django.template.defaultfilters import title
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.views import APIView

# Create your tests here.
from .models import  Category, Goal, Task

class GoalTaskAPI(APITestCase):
    def setUp(self):
        # Create two users
        self.user1 = User.objects.create_user(
            username ="user1",
            password ="testpass123"
        )
        self.user2 = User.objects.create_user(
            username ="user2",
            password ="testpass123"
        )

        #create one category
        self.category = Category.objects.create(name="Work")

        #create goals for each user
        self.goal1 = Goal.objects.create(
            title = "User1 goal title",
            description = "User1 goal description",
            category = self.category,
            user = self.user1,
        )
        self.goal2 =Goal.objects.create(
            title = "User2 goal title",
            description = "User2 goal description",
            category = self.category,
            user = self.user2,
        )

        #create tasks for each user' goal
        self.task1 = Task.objects.create(
            title = "User1 task title",
            description = "User1 task description",
            completed = False,
            goal = self.goal1,
        )
        self.task2 = Task.objects.create(
            title = "User2 task title",
            description = "User2 task description",
            completed = False,
            goal = self.goal2,
        )

    def test_authentication_required_for_goals(self):
        ## Unauthenticated user should not access goals list.##
        url = reverse("goal-list-create")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_user_sees_only_own_goals(self):
        ## Authenticated user should see only their own goals. ##
        self.client.force_authenticate(user=self.user1)

        url = reverse("goal-list-create")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)
        self.assertEqual(response.data["results"][0]["title"], "User1 goal title")

    def test_user_cannot_create_task_for_another_users_goal(self):
        ## User should not be able to create a task for someone else's goal. ##
        self.client.force_authenticate(user=self.user1)
        url = reverse("task-list-create")
        data = {
            "tittle": "Hack tittle",
            "description": "Hack description",
            "completed": False,
            "goals": self.goal2.id
        }

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("goal", response.data)

    def test_user_cannot_access_another_users_goal_detail(self):
        self.client.force_authenticate(user=self.user1)

        url = reverse('goal-detail', kwargs={'pk': self.goal2.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_cannot_access_another_users_task_detail(self):
        self.client.force_authenticate(user=self.user1)

        url = reverse('task-detail', kwargs={'pk': self.task2.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_cannot_update_task_with_another_users_goal(self):
        self.client.force_authenticate(user=self.user1)

        url = reverse('task-detail', kwargs={'pk': self.task1.id})
        data = {
            'title': 'Updated task',
            'description': 'Trying to move task',
            'completed': True,
            'goal': self.goal2.id
        }

        response = self.client.patch(url, data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('goal', response.data)