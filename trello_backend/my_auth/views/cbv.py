from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from my_auth.serializers import MyUserSerializer
from my_auth.models import MyUser


class MyUserAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = MyUserSerializer

    def get_queryset(self):
        return MyUser.objects.all()

    def perform_create(self, serializer):
        username = self.request.data.pop('username')
        password = self.request.data.pop('password')
        # email = self.request.data.pop('email')
        user, created = MyUser.objects.get_or_create(username=username)
        # user.set_email(email)
        user.set_password(password)
        user.save()


class ChangePasswordAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def put(self, request):
        user = MyUser.objects.get(username=request.user.username)
        new_password = self.request.data.pop('new_password')
        user.set_password(new_password)
        user.save()
        return Response({}, status=status.HTTP_200_OK)

