from .models import Board,List,Task
from rest_framework import serializers
from my_auth.serializers import MyUserSerializer


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ('id','title', 'created_at','status')

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = ('id','title','board','on_review')

class TaskSerializer(serializers.ModelSerializer):
    owner = MyUserSerializer(read_only=True)

    class Meta:
        model = Task
        fields = ('id','title','description','dueDate','created_at','attachment', 'image', 'owner','assigned','list')
