from rest_framework import generics

from product.models import Product
from product.api.v1.serializers import ProductSerializer


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
