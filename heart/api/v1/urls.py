from django.urls import path

from heart.api.v1 import views

app_name = 'heart-v1'

urlpatterns = [
    path('toggle/', views.ToggleHeartAPIView.as_view(), name='toggle'),
    path('hearted/', views.UserHeartedProductsListAPIView.as_view(), name='hearted'),
    path('recommended/', views.RecommendedProductsListAPIView.as_view(), name='recommended'),
]
