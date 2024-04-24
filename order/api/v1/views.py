from rest_framework import generics

from order.models import Order
from order.api.v1.serializers import OrderSerializer


class UserOrderListAPIView(generics.ListAPIView):
    """
    API endpoint to list all orders of the authenticated user.
    """

    serializer_class = OrderSerializer

    def get_queryset(self):
        # Optimization FTW!
        return self.request.user.orders.all().prefetch_related('items').prefetch_related('items__product')


class OrderCheckoutAPIView(generics.CreateAPIView):
    """
    API endpoint to checkout the authenticated user's cart.
    """

    queryset = Order.objects.none()
    serializer_class = OrderSerializer
