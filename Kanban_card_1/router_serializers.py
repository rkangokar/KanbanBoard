from rest_framework import serializers
from Kanban_card_1.models import Card, Task

class TaskSerializer(serializers.ModelSerializer):
    card = serializers.HyperlinkedRelatedField(
        queryset=Card.objects.all(),
        view_name='card-detail'
    )
    
    class Meta:
        model = Task
        fields = '__all__'

class CardSerializer(serializers.ModelSerializer):
    tasks = serializers.HyperlinkedRelatedField(
        queryset=Task.objects.all(),
        many=True,
        view_name='task-detail'
    )
    owner = serializers.ReadOnlyField(source='owner.username')
    
    class Meta:
        model = Card
        fields = '__all__'