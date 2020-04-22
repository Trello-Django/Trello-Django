from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.decorators import action
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from rest_framework.response import Response


from rest_framework.permissions import IsAuthenticated

from .models import Board, List,Task
from .serializers import BoardSerializer, TaskSerializer, ListSerializer


class BoardViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                       mixins.CreateModelMixin, mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin, viewsets.GenericViewSet):

    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = (IsAuthenticated,)

    @action(methods=['GET', 'POST'], detail=True)
    def lists(self, request, pk):
        pkk = self.kwargs.get('pk')

        try:
            list = List.objects.filter(board = Board.objects.get(id=pkk))
        except ObjectDoesNotExist:
            raise Http404
        serializer = ListSerializer(list, many=True)
        return Response(serializer.data)



class ListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                       mixins.CreateModelMixin, mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin, viewsets.GenericViewSet):

    queryset = List.objects.all()
    serializer_class = ListSerializer
    permission_classes = (IsAuthenticated,)

    @action(methods=['GET', 'POST'], detail=True)
    def tasks(self, request, pk):
        try:
            task = Task.objects.filter(list = List.objects.get(id=pk))
        except ObjectDoesNotExist:
            raise Http404
        serializer = TaskSerializer(task, many=True)
        return Response(serializer.data)



class TaskViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                       mixins.CreateModelMixin, mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin, viewsets.GenericViewSet):

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)


