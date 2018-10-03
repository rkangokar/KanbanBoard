from rest_framework import serializers
from Kanban_card_1.models import Card, Task
 
# class CardSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Card
#         fields = '__all__'
        
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        
class CardSerializer(serializers.ModelSerializer):
    tasks = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    tasks = serializers.StringRelatedField(many=True)
    tasks = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')
    tasks = TaskSerializer(many=True, read_only=True)
     
    class Meta:
        model = Card
        fields = '__all__'