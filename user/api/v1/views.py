from rest_framework import generics
from rest_framework.permissions import AllowAny

from user.models import User
from user.api.v1.serializers import UserCreateSerializer


class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.none()
    permission_classes = (AllowAny,)
    serializer_class = UserCreateSerializer
