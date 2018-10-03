from django.conf.urls import url
# from Kanban_card_1 import views
 
# urlpatterns = [
#     url(r'^cards$', views.card_collection),
#     url(r'^cards/(?P<id>[0-9]+)$', views.card_item),
#     url(r'^tasks', views.task_collection),
# ]

from rest_framework_jwt.views import obtain_jwt_token
from Kanban_card_1 import generic_views
     
urlpatterns = [
    url(
        r'^cards',
        generic_views.CardList.as_view(),
        name=generic_views.CardList.name
    ),
    url(
        r'^cards/(?P<pk>[0-9]+)$',
        generic_views.CardDetail.as_view(),
        name=generic_views.CardDetail.name
    ),
    url(
        r'^tasks',
        generic_views.TaskList.as_view(),
        name=generic_views.TaskList.name
    ),
    url(
        r'^tasks/(?P<pk>[0-9]+)$',
        generic_views.TaskDetail.as_view(),
        name=generic_views.TaskDetail.name
    ),
    url(
        r'^jwt-token$', 
        obtain_jwt_token
    )
]