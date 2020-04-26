from rest_framework.viewsets import ModelViewSet
from rest_framework_extensions.mixins import NestedViewSetMixin
from rest_framework.permissions import IsAuthenticated

from .models import Board, List, Task
from .serializers import BoardSerializer, TaskSerializer, ListSerializer

import logging
logger = logging.getLogger('core')


class BoardViewSet(NestedViewSetMixin, ModelViewSet):

    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save()
        logger.info(f'Board with id = {serializer.data["id"]} created')

    def perform_update(self, serializer):
        serializer.save()
        logger.info(f'Board with id = {serializer.data["id"]} updated')

    def perform_destroy(self, instance):
        instance.delete()
        logger.info(f'Board with id = {instance.id} deleted')


class ListViewSet(NestedViewSetMixin, ModelViewSet):

    serializer_class = ListSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return List.objects.filter(board=self.kwargs.get('parent_lookup_board'))

    def perform_create(self, serializer):
        logger.info(f'List with id = {serializer.data["id"]} created')
        serializer.save(board_id=self.kwargs.get('parent_lookup_board'))

    def perform_update(self, serializer):
        serializer.save()
        logger.info(f'List with id = {serializer.data["id"]} updated')

    def perform_destroy(self, instance):
        instance.delete()
        logger.info(f'List with id = {instance.id} deleted')


class TaskViewSet(NestedViewSetMixin, ModelViewSet):

    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Task.objects.filter(list=self.kwargs.get('parent_lookup_list'))

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user, list_id=self.kwargs.get('parent_lookup_list'))
        logger.info(f'Task with id = {serializer.data["id"]} created')

    def perform_update(self, serializer):
        serializer.save()
        logger.info(f'Task with id = {serializer.data["id"]} updated')

    def perform_destroy(self, instance):
        instance.delete()
        logger.info(f'Task with id = {instance.id} deleted')

