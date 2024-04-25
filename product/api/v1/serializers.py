from typing import Optional

from rest_framework import serializers

from user.models import User
from heart.models import Heart
from product.models import Product


class ProductSerializer(serializers.ModelSerializer):

    is_hearted = serializers.SerializerMethodField()

    def get_is_hearted(self, product: Product) -> Optional[bool]:

        if hasattr(product, Product.IS_HEARTED_ANNOTATION):
            print(getattr(product, Product.IS_HEARTED_ANNOTATION))
            return getattr(product, Product.IS_HEARTED_ANNOTATION)

        if 'request' in self.context:

            user: User = self.context['request'].user

            if user.is_authenticated:
                return Heart.objects.filter(user=user, product=product).exists()

            return None

        return None

    class Meta:
        model = Product
        exclude = ('updated_at',)


class ProductDetailSerializer(serializers.ModelSerializer):

    users_also_bought = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        exclude = ('updated_at',)
