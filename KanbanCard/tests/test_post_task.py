from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from KanbanCard.models import Card
from test_utils import get_card, post_card, post_task

class PostTaskTests(APITestCase):
    def setUp(self):
        self.username = 'Avi'
        self.user = User.objects.create(
            username=self.username,
            password='avipwd'
        )
        self.title = 'KanbanCard : Education'
        self.description = 'Knowledge is power'
        self.task = []
        self.client.force_authenticate(self.user)
        self.response = post_card(self.client, self.title, self.description, self.task)

    def test_postTask(self):
        name = "Right to education"
        response = post_task(APIClient(), self.response.data['id'], name)
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['name'] == name