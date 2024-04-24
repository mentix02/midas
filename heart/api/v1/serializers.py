from rest_framework import serializers

from product.models import Product


class HeartToggleSerializer(serializers.Serializer):

    # True indicates heart is added, False indicates heart is removed
    result = serializers.BooleanField(read_only=True)
    product_id = serializers.IntegerField(required=True, write_only=True)

    def validate_product_id(self, value: int) -> int:
        if value < 1:
            raise serializers.ValidationError('Product ID must be greater than 0')
        if not Product.objects.filter(id=value).exists():
            raise serializers.ValidationError('Product does not exist')
        return value
