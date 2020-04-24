from rest_framework.decorators import action
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from rest_framework.response import Response
from rest_framework import viewsets, mixins
from rest_framework_extensions.mixins import NestedViewSetMixin
from rest_framework.permissions import IsAuthenticated
from homepage.models import Team, Profile
from homepage.serializers import TeamSerializer, ProfileSerializer


class ProfileViewSet(viewsets.ModelViewSet):

    permission_classes = (IsAuthenticated,)
    query_set = Profile.objects.all()
    serializer_class = ProfileSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(methods=['GET', 'POST'], detail=True)
    def change_role(self, request):
        try:
            profile = Profile.objects.get(id=self.kwargs['pk'])
        except ObjectDoesNotExist:
            raise Http404
        print(request)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)


class TeamViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    query_set = Team.objects.all()
    serializer_class = TeamSerializer

    def perform_create(self, serializer):
        serializer.save()


class TeamMemberViewSet(NestedViewSetMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProfileSerializer

    def get_queryset(self):
        return Profile.objects.filter(list=self.kwargs.get('parent_lookup_team'))
