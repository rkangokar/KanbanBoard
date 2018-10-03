from rest_framework import generics, permissions
from django.core import exceptions

from KanbanCard.models import Card, Task
from KanbanCard.serializers import CardSerializer, TaskSerializer
from KanbanCard import custom_permission


class CardList(generics.ListCreateAPIView):
    serializer_class = CardSerializer
    name = 'card-list'
    
    permission_classes = (
        permissions.IsAuthenticated,
    )
    
    def get_queryset(self):
        return Card.objects.filter(owner=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
class CardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    name = 'card-detail'
    
    permission_classes = (
        permissions.IsAuthenticated,
        custom_permission.IsCurrentUserOwner
    )
    
class TaskList(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    name = 'task-list'
    
    permission_classes = (
        permissions.IsAuthenticated,
    )
    
    def perform_create(self, serializer):
        if serializer.validated_data['card'].owner != self.request.user:
            raise exceptions.PermissionDenied()
        serializer.save()
        
    
class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    name = 'task-detail'
    
    permission_classes = (
        permissions.IsAuthenticated,
        custom_permission.IsCurrentUserAccountOwner
    )