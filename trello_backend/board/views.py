from rest_framework import viewsets
from rest_framework import mixins
from .models import Board, List,Task
from .serializers import BoardSerializer, TaskSerializer, ListSerializer


from rest_framework.permissions import IsAuthenticated


class BoardListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                       mixins.CreateModelMixin, mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer



    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)


class ListListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                       mixins.CreateModelMixin, mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer



class TaskListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                       mixins.CreateModelMixin, mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin, viewsets.GenericViewSet):

    queryset = Task.objects.all()
    serializer_class = TaskSerializer



    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)



