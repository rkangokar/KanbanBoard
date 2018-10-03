# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Kanban_card_1.models import Card, Task
from Kanban_card_1.serializers import CardSerializer, TaskSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def card_collection(request):
    if request.method == 'GET':
        cards = Card.objects.all()
        cards_serializer = CardSerializer(cards, many=True)
        return Response(cards_serializer.data)
    elif request.method == 'POST':
        card_serializer = CardSerializer(data=request.data)
        if card_serializer.is_valid():
            card_serializer.save()
            return Response(card_serializer.data, status=status.HTTP_201_CREATED)
        return Response(card_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        cards = Card.objects.all().delete()

@api_view(['GET', 'PUT', 'DELETE'])
def card_item(request, id):
    try:
        card = Card.objects.get(pk=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        card_serializer = CardSerializer(card)
        return Response(card_serializer.data)
    elif request.method == 'PUT':
        card_serializer = CardSerializer(card, data=request.data)
        if card_serializer.is_valid():
            card_serializer.save()
            return Response(card_serializer.data)
        return Response(card_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        card.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET', 'POST'])
def task_collection(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        tasks_serializer = TaskSerializer(tasks, many=True)
        return Response(tasks_serializer.data)
    elif request.method == 'POST':
        task_serializer = TaskSerializer(data=request.data)
        if task_serializer.is_valid():
            task_serializer.save()
            return Response(task_serializer.data, status=status.HTTP_201_CREATED)
        return Response(task_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def task_item(request, id):
    try:
        task = Task.objects.get(pk=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        task_serializer = TaskSerializer(task)
        return Response(task_serializer.data)
    elif request.method == 'PUT':
        task_serializer = TaskSerializer(task, data=request.data)
        if task_serializer.is_valid():
            task_serializer.save()
            return Response(task_serializer.data)
        return Response(task_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)