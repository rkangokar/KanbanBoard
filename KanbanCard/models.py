from django.db import models


class Card(models.Model):
    TYPE_TODO = 'to-do'
    TYPE_INPROCESS = 'in-process'
    TYPE_DONE = 'done'
    TYPE_CHOICES = (
        (TYPE_TODO, 'to-do'),
        (TYPE_INPROCESS, 'in-process'),
        (TYPE_DONE, 'done')
    )
    
    title = models.CharField(unique=True, max_length=150, blank=False)
    description = models.CharField(max_length=250, blank=True)
    status = models.CharField(max_length=20, choices=TYPE_CHOICES, default=TYPE_TODO)
    owner = models.ForeignKey(
        'auth.User',
        related_name='cards',
        on_delete=models.CASCADE,
        null = True
        )
    
class Task(models.Model):
    name = models.CharField(max_length=150,blank=False)
    done = models.BooleanField(default=False)
    card = models.ForeignKey(
        Card,
        related_name='tasks',
        on_delete=models.CASCADE
    )
    
    class Meta:
        unique_together = ('card', 'name')