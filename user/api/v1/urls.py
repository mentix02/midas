from django.urls import path

from rest_framework.authtoken.views import ObtainAuthToken

from user.api.v1.views import UserCreateAPIView

app_name = 'user-v1'

urlpatterns = [
    path('token/', ObtainAuthToken.as_view(), name='token'),
    path('create/', UserCreateAPIView.as_view(), name='create'),
]
