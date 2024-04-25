from django.db.models import OuterRef, Case, When, Value, BooleanField

from rest_framework import generics
from rest_framework.permissions import AllowAny

from heart.models import Heart
from product.models import Product
from product.api.v1.serializers import ProductSerializer, ProductDetailSerializer


class ProductListAPIView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ProductSerializer

    def get_queryset(self):
        user = self.request.user

        if not user.is_authenticated:
            return Product.objects.all()

        return Product.objects.annotate(
            **{
                Product.IS_HEARTED_ANNOTATION: Case(
                    When(hearts__user=user, then=Value(True)),
                    default=Value(False),
                    output_field=BooleanField(),
                ),
            }
        ).prefetch_related('hearts')


class ProductRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = ProductDetailSerializer
