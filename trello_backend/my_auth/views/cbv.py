from rest_framework import generics
from rest_framework.permissions import AllowAny
from my_auth.serializers import MyUserSerializer
from my_auth.models import MyUser


class MyUserAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = MyUserSerializer

    def get_queryset(self):
        return MyUser.objects.all()

    def perform_create(self, serializer):
        serializer.save()


