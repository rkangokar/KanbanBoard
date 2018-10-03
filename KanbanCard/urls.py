from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token

from KanbanCard import views

urlpatterns = [
    url(
        r'^cards$',
        views.CardList.as_view(),
        name=views.CardList.name
    ),
    url(
        r'^cards/(?P<pk>[0-9]+)$',
        views.CardDetail.as_view(),
        name=views.CardDetail.name
    ),
    url(
        r'^tasks$',
        views.TaskList.as_view(),
        name=views.TaskList.name
    ),
    url(
        r'^tasks/(?P<pk>[0-9]+)$',
        views.TaskDetail.as_view(),
        name=views.TaskDetail.name
    )
#    , url(
#         r'^jwt-token$', 
#         obtain_jwt_token
#     )
]