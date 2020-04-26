from .models import Team, Profile
from rest_framework import serializers
from core.serializers import BoardSerializer
from my_auth.serializers import MyUserSerializer
from core.models import Board
import re


class TeamSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255, required=True)
    created_at = serializers.DateTimeField(required=False)
    board_id = serializers.IntegerField(read_only=True)
    board = BoardSerializer(required=False)

    def create(self, validated_data):
        team = Team(**validated_data)
        team.save()
        return team

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        board_id = validated_data.get('board_id', instance.board_id)
        instance.board_id = board_id
        board = Board.objects.get(id=board_id)
        instance.board = board
        instance.save()
        return instance


class ProfileSerializer(serializers.ModelSerializer):
    avatar = serializers.ImageField(required=False)
    name = serializers.CharField(required=True)
    surname = serializers.CharField(required=True)
    date_of_birth = serializers.DateField(required=False)
    phone = serializers.CharField(required=False)
    role = serializers.CharField(required=True)
    user = MyUserSerializer(required=False)
    team = TeamSerializer(required=False)

    class Meta:
        model = Profile
        fields = '__all__'

    def validate_phone(self, value):
        pattern = re.compile("^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\s\./0-9]*$")
        if not pattern.match(value):
            raise serializers.ValidationError("Phone number does not match pattern, pattern: +7 747 589 6699")
        return value

    def validate_name(self, value):
        pattern = re.compile("^[A-Za-z-]+$")
        if not pattern.match(value):
            raise serializers.ValidationError("Only A-Z, a-z, - symbols are allowed")
        return value

    def validate_surname(self, value):
        pattern = re.compile("^[A-Za-z-]+$")
        if not pattern.match(value):
            raise serializers.ValidationError("Only A-Z, a-z, - symbols are allowed")
        return value
