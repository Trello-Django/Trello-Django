from rest_framework import serializers
from my_auth.models import MyUser


class MyUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyUser
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = MyUser.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def validate_username(self, value):
        if not len(value) >= 5:
            raise serializers.ValidationError("Username should contain more than 4 symbols")
        return value
