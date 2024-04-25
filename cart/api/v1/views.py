from django.db.models.query import QuerySet

from rest_framework import generics
from rest_framework.permissions import SAFE_METHODS

from cart.api.v1.serializers import CartItemSerializer, CartItemReadSerializer


class CartItemListCreateAPIView(generics.ListCreateAPIView):

    def get_serializer_class(self):
        return CartItemReadSerializer if self.request.method in SAFE_METHODS else CartItemSerializer

    def get_queryset(self) -> QuerySet:
        return self.request.user.cart.all().select_related('product')


class CartItemRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    def get_serializer_class(self):
        return CartItemReadSerializer if self.request.method in SAFE_METHODS else CartItemSerializer

    def get_queryset(self) -> QuerySet:
        return self.request.user.cart.all()
