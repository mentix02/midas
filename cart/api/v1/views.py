from django.db.models.query import QuerySet

from rest_framework import generics

from cart.api.v1.serializers import CartItemSerializer


class CartItemListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = CartItemSerializer

    def get_queryset(self) -> QuerySet:
        return self.request.user.cart.all()


class CartItemRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CartItemSerializer

    def get_queryset(self) -> QuerySet:
        return self.request.user.cart.all()
