# from rest_framework import generics
# from Kanban_card_1.models import Card, Task
# from Kanban_card_1.serializers import CardSerializer, TaskSerializer

# class CardList(generics.ListCreateAPIView):
#     queryset = Card.objects.all()
#     serializer_class = CardSerializer
#     name = 'card-collection'
#     ordering_fields = (
#         'title',
#     )
#     
# class CardDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Card.objects.all()
#     serializer_class = CardSerializer
#     name = 'card-item'
#     
# class TaskList(generics.ListCreateAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
#     name = 'task-collection'
#     
# class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
#     name = 'task-item'
    
    
    
from rest_framework import generics, permissions
from django.core import exceptions

from Kanban_card_1.models import Card, Task
from Kanban_card_1.router_serializers import CardSerializer, TaskSerializer
from Kanban_card_1 import custom_permission


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