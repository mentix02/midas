from rest_framework import serializers

from cart.models import CartItem
from product.api.v1.serializers import ProductSerializer


class CartItemSerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    quantity = serializers.IntegerField(default=1, required=False, initial=1)

    def create(self, validated_data):
        # check if product is already in cart
        product = validated_data.get('product')
        user = validated_data.get('user')

        if user.cart.filter(product=product).exists():
            cart_item: CartItem = user.cart.get(product=product)
            cart_item.increment_quantity(validated_data.get('quantity', 1))
            return cart_item

        return super().create(validated_data)

    class Meta:
        model = CartItem
        read_only_fields = ('id',)
        fields = ('id', 'user', 'product', 'quantity')


class CartItemReadSerializer(serializers.ModelSerializer):

    product = ProductSerializer()

    class Meta:
        model = CartItem
        fields = ('id', 'product', 'quantity')
