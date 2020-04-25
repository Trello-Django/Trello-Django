from rest_framework.decorators import action
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from rest_framework.response import Response
from rest_framework import viewsets, mixins
from rest_framework_extensions.mixins import NestedViewSetMixin
from rest_framework.permissions import IsAuthenticated
from homepage.models import Team, Profile
from homepage.serializers import TeamSerializer, ProfileSerializer
from core.models import Board

import logging
logger = logging.getLogger('homepage')


class ProfileViewSet(viewsets.ModelViewSet):

    permission_classes = (IsAuthenticated,)
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        logger.info(f'Profile with id = {serializer.data["id"]} created')

    def perform_update(self, serializer):
        try:
            profile = Profile.objects.get(id=self.kwargs['pk'])
        except ObjectDoesNotExist:
            raise Http404
        role = profile.role
        serializer.save(role=role)
        logger.info(f'Profile with id = {serializer.data["id"]} updated')

    @action(methods=['PUT'], detail=True)
    def change_role(self, request, pk):
        role = request.data.pop('role')
        try:
            profile = Profile.objects.filter(id=pk)
        except ObjectDoesNotExist:
            raise Http404
        profile.update(role=role)
        logger.info(f'Profile with id = {profile[0].id} changed role')
        return Response({'status': 'role has been changed'}, status=200)


class TeamViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    def perform_create(self, serializer):
        serializer.save(board_id=self.request.data.get('board_id'))
        logger.info(f'Team with id = {serializer.data["id"]} created')

    def perform_update(self, serializer):
        try:
            board = Board.objects.get(id=self.request.data.get('board_id'))
            serializer.save(board_id=board.id)
            logger.info(f'Team with id = {serializer.data["id"]} updated')
        except Board.DoesNotExist:
            raise Http404


class TeamMemberViewSet(NestedViewSetMixin,
                        mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProfileSerializer

    def get_queryset(self):
        return Profile.objects.filter(team_id=self.kwargs.get('parent_lookup_team'))

    def perform_update(self, serializer):
        serializer.save()
        logger.info(f'Team member(Profile) with id = {serializer.data["id"]} updated')

    def perform_destroy(self, instance):
        instance.delete()
        logger.info(f'Team member(Profile) with id = {instance.data["id"]} deleted')

