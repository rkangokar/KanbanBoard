from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from KanbanCard.models import Card
from test_utils import post_card

class PostCardTest(APITestCase):
    def setUp(self):
        self.username = 'Reshma'
        self.user = User.objects.create(
            username=self.username,
            password='reshpwd'
        )
    
    def test_post_card_anonymously(self):
        title = 'KanbanCard : Health'
        description = 'Health is Wealth'
        task = []
        response = post_card(self.client, title, description, task)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert Card.objects.count() == 0
        
    def test_post_card(self):
        title = 'KanbanCard : Health'
        description = 'Health is Wealth'
        task = []
        self.client.force_authenticate(user=self.user)
        response = post_card(self.client, title, description, task)
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['owner'] == self.username
        assert response.data['title'] == title
        assert Card.objects.count() == 1
        assert Card.objects.get().title == title