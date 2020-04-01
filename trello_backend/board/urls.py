from django.urls import path


from rest_framework.routers import DefaultRouter

from .views import BoardListViewSet,ListListViewSet,TaskListViewSet

router = DefaultRouter()

router.register(r'boards',BoardListViewSet)
router.register(r'lists',ListListViewSet)
router.register(r'tasks',TaskListViewSet)

urlpatterns = router.urls
