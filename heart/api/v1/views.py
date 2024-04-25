from django.db.models import Value, QuerySet

from rest_framework import status
from rest_framework import generics
from rest_framework.request import Request
from rest_framework.response import Response

from user.models import User
from product.models import Product
from recommender import Recommender
from product.api.v1.serializers import ProductSerializer
from heart.api.v1.serializers import HeartToggleSerializer


class RecommendedProductsListAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self) -> QuerySet:
        recommender = Recommender()
        user: User = self.request.user
        recommended_product_ids = recommender.recommend(user.id)
        # annotate with a False since the recommender only suggests
        # products which aren't already liked by the user.
        return Product.objects.filter(id__in=recommended_product_ids).annotate(
            **{Product.IS_HEARTED_ANNOTATION: Value(False)}
        )


class ToggleHeartAPIView(generics.CreateAPIView):
    """
    _Toggle_ heart for a product.
    Result returns True if a heart was added, False if a heart was removed.
    """

    serializer_class = HeartToggleSerializer

    def create(self, request: Request, *args, **kwargs) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user: User = request.user
        product_id = serializer.validated_data['product_id']
        result = user.toggle_product_heart(product_id)

        return Response({'result': result}, status=status.HTTP_201_CREATED if result else status.HTTP_200_OK)


class UserHeartedProductsListAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self) -> QuerySet:
        user: User = self.request.user
        return Product.objects.filter(hearts__user=user).annotate(**{Product.IS_HEARTED_ANNOTATION: Value(True)})
