from django.urls import path

from order.api.v1 import views

app_name = 'order-v1'

urlpatterns = [
    path('', views.UserOrderListAPIView.as_view(), name='list'),
    path('checkout/', views.OrderCheckoutAPIView.as_view(), name='checkout'),
]
