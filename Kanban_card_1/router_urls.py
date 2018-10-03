from rest_framework import routers
from Kanban_card_1.router_viewsets import CardViewSet, TaskViewSet

router = routers.SimpleRouter()
router.register(r'cards', CardViewSet)
router.register(r'tasks', TaskViewSet)
urlpatterns = router.urls