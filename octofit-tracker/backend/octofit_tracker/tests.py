from django.urls import reverse
from rest_framework.test import APITestCase
from .models import Team, User, Activity, Workout, Leaderboard

class APIRootTest(APITestCase):
    def test_api_root(self):
        url = reverse('api-root')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('teams', response.data)
        self.assertIn('users', response.data)
        self.assertIn('activities', response.data)
        self.assertIn('workouts', response.data)
        self.assertIn('leaderboard', response.data)

class TeamTest(APITestCase):
    def test_team_list(self):
        Team.objects.create(name='Marvel')
        url = reverse('team-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data), 1)
