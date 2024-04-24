from rest_framework import serializers

from cart.models import CartItem


class CartItemSerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    quantity = serializers.IntegerField(default=1, required=False, initial=1)

    class Meta:
        model = CartItem
        read_only_fields = ('id', 'timestamp')
        fields = ('id', 'user', 'product', 'quantity', 'timestamp')
