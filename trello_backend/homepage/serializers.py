from .models import Team, Profile
from rest_framework import serializers
from core.serializers import BoardSerializer
from my_auth.serializers import MyUserSerializer


class TeamSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255, required=True)
    created_at = serializers.DateTimeField(required=False)
    board = BoardSerializer(required=False)

    class Meta:
        model = Team
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    avatar = serializers.ImageField(required=False)
    name = serializers.CharField(required=True)
    surname = serializers.CharField(required=True)
    date_of_birth = serializers.DateField(required=False)
    phone = serializers.CharField(required=False)
    role = serializers.CharField(required=True)
    user = MyUserSerializer(required=False)
    team_id = serializers.IntegerField(required=True)
    team = TeamSerializer(required=False)

    class Meta:
        model = Profile
        fields = '__all__'
