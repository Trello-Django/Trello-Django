from .models import Board,List,Task
from rest_framework import serializers
from my_auth.serializers import MyUserSerializer


class BoardSerializer(serializers.ModelSerializer):
    owner = MyUserSerializer(read_only=True)
    # reviewer = MyUserSerializer(read_only=True)
    class Meta:
        model = Board
        fields = ('title','owner','reviewer')

class ListSerializer(serializers.ModelSerializer):
    # board = BoardSerializer(write_only=True)

    class Meta:
        model = List
        fields = ('title','board')


class TaskSerializer(serializers.ModelSerializer):
    owner = MyUserSerializer(read_only=True)
    list = ListSerializer

    class Meta:
        model = Task
        fields = ('title','owner','list','description','dueDate','created_at',)
