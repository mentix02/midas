from django.urls import path

from cart.api.v1 import views

app_name = 'cart-v1'

urlpatterns = [
    path('', views.CartItemListCreateAPIView.as_view(), name='list-create'),
    path('<int:pk>/', views.CartItemRetrieveUpdateDestroyAPIView.as_view(), name='retrieve-update-destroy'),
]
