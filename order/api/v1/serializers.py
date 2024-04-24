from rest_framework import serializers

from order.models import Order, OrderItem
from product.api.v1.serializers import ProductSerializer


class OrderItemSerializer(serializers.ModelSerializer):

    product = ProductSerializer()

    class Meta:
        model = OrderItem
        fields = ('id', 'product', 'quantity')


class OrderSerializer(serializers.ModelSerializer):

    items = OrderItemSerializer(many=True, read_only=True)

    def create(self, _) -> Order:
        try:
            return self.context['request'].user.checkout()
        except ValueError as e:
            raise serializers.ValidationError(str(e))

    class Meta:
        model = Order
        fields = ('id', 'items', 'total')
