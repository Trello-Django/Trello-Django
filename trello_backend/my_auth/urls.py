from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token

from my_auth import views


urlpatterns = [
    path('login/', obtain_jwt_token),
    path('register/', views.MyUserAPIView.as_view())
]

