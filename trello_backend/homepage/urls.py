
from rest_framework_extensions.routers import ExtendedSimpleRouter

from .views import TeamViewSet, ProfileViewSet, TeamMemberViewSet

router = ExtendedSimpleRouter()


router.register(r'team', TeamViewSet, basename='team').\
    register(r'member', TeamMemberViewSet, basename='member', parents_query_lookups=['team'])


router.register(r'profile', ProfileViewSet, basename='profile')

urlpatterns = router.urls

