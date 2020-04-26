from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.decorators import action
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from rest_framework_extensions.mixins import NestedViewSetMixin
from rest_framework.permissions import IsAuthenticated

from .models import Board, List, Task
from .serializers import BoardSerializer, TaskSerializer, ListSerializer


class BoardViewSet(NestedViewSetMixin, ModelViewSet):

    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = (IsAuthenticated,)


class ListViewSet(NestedViewSetMixin, ModelViewSet):

    serializer_class = ListSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return List.objects.filter(board=self.kwargs.get('parent_lookup_board'))

    def perform_create(self, serializer):
        serializer.save(board_id=self.kwargs.get('parent_lookup_board'))


class TaskViewSet(NestedViewSetMixin, ModelViewSet):

    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Task.objects.filter(list=self.kwargs.get('parent_lookup_list'))

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user, list_id=self.kwargs.get('parent_lookup_list'))

    #
    # @action(methods=['PUT'], detail=True)
    # def complete_task(self, request, pk, parent_lookup_list):
    #     pkk = self.kwargs.get('pk')
    #     print(pkk)
    #     try:
    #         task = Task.objects.filter(id = pkk)
    #     except ObjectDoesNotExist:
    #         raise Http404
    #     serializer = TaskSerializer(task, many = True)
    #     if serializer.is_valid():
    #         serializer.save(completed=False)
    #
    #     return Response(serializer.data)
