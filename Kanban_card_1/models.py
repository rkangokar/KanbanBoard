# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Card(models.Model):
    TYPE_TODO = 'to-do'
    TYPE_INPROCESS = 'in-process'
    TYPE_DONE = 'done'
    TYPE_CHOICES = (
        (TYPE_TODO, 'to-do'),
        (TYPE_INPROCESS, 'in-process'),
        (TYPE_DONE, 'done')
    )
    
    title = models.CharField(blank=False, unique=True, max_length=150)
    description = models.CharField(blank=True, max_length=250)
    status = models.CharField(max_length=20, choices=TYPE_CHOICES, default=TYPE_TODO)
    owner = models.ForeignKey(
        'auth.User',
        related_name='cards',
        on_delete=models.CASCADE,
        null = True
        )
    
    def __str__(self):
        return str(self.id) + ' ' + self.title + ' ' + self.description + ' ' + self.status
    
    class Meta:
        ordering = ('title',)
    
class Task(models.Model):
    name = models.CharField(max_length=250,blank=False)
    done = models.BooleanField(default=False)
    card = models.ForeignKey(
        Card,
        related_name = "tasks",
        on_delete=models.CASCADE
        )
    
    def __str__(self):
        return str(self.name + ' ' + self.done)
    
    class Meta:
        unique_together = ('card', 'name')