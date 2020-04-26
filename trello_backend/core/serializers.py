from .models import Board, List, Task
from rest_framework import serializers
from my_auth.serializers import MyUserSerializer


class BoardSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=300)
    created_at = serializers.DateTimeField
    status = serializers.IntegerField(required=False)

    def create(self, validated_data):
        board = Board(**validated_data)
        board.save()
        return board

    def update(self, instance,validated_data):
        instance.name = validated_data.get('title', instance.title)
        instance.type = validated_data.get('status', instance.status)
        instance.save()
        return instance


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = ('id', 'title', 'board', 'on_review')


class TaskSerializer(serializers.ModelSerializer):
    owner = MyUserSerializer(read_only=True)
    list = ListSerializer(read_only=True)

    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'dueDate', 'created_at', 'attachment', 'image', 'owner', 'assigned',
                  'list', 'completed')
