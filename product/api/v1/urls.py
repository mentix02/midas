from django.urls import path

from product.api.v1 import views

app_name = 'product-v1'

urlpatterns = [
    path('', views.ProductListAPIView.as_view(), name='list'),
    path('<int:pk>/', views.ProductRetrieveAPIView.as_view(), name='retrieve'),
]
