from django.urls import path

from heart.api.v1.views import ToggleHeartAPIView, UserHeartedProductsListAPIView

app_name = 'heart-v1'

urlpatterns = [
    path('toggle/', ToggleHeartAPIView.as_view(), name='toggle'),
    path('hearted/', UserHeartedProductsListAPIView.as_view(), name='hearted'),
]
