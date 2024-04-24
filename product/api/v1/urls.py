from django.urls import path

from product.api.v1.views import ProductListAPIView

app_name = 'product-v1'

urlpatterns = [
    path('', ProductListAPIView.as_view(), name='list'),
]
