from django.urls import reverse
from django.utils.http import urlencode
from KanbanCard import views

def post_card(client, title, description, task):
    data = { 'title': title, 'description': description, 'tasks': task }
    url = reverse(views.CardList.name)
    response = client.post(url, data, format='json')
    return response
    
def get_card(client):
    url = reverse(views.CardList.name)
    response = client.get(url, format='json')
    return response
    
def get_card_by_title(client, keyword):
    url = reverse(views.CardList.name)
    #url = '{}?{}'.format(url, urlencode({ 'title': keyword }))
    url = '{}?title=Health'.format(url)
    response = client.get(url, format='json')
    return response
    
def get_card(client, id):
    url = reverse(views.CardDetail.name, args=[id])
    response = client.get(url, format='json')
    return response
    
def post_task(client, card_id, task_name):
    url = reverse(views.TaskList.name)
    data = { 'card': "https://localhost:8000/cards/"+str(card_id), 'name': task_name }
    response = client.post(url, data, format='json')
    return response