
from rest_framework_extensions.routers import ExtendedSimpleRouter

from .views import BoardViewSet,ListViewSet,TaskViewSet

router = ExtendedSimpleRouter()

router.register(r'boards', BoardViewSet, basename='board').\
    register(r'lists', ListViewSet, basename='board-list', parents_query_lookups=['board'])

router.register(r'lists', ListViewSet, basename='list').\
    register(r'tasks', TaskViewSet, basename='list-task', parents_query_lookups=['list'])

urlpatterns = router.urls

