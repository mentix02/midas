from typing import Optional

import numpy as np
from lightfm import LightFM
from lightfm.data import Dataset

from user.models import User
from heart.models import Heart
from product.models import Product


class Recommender:
    """
    This Recommender is a product of Googling and reading LightFM's
    god-awful documentation after 6 hours with a fever and a headache.

    It's not performant? Too bad. It's not accurate? Too bad. It's not
    scalable? Too bad. It's not maintainable? Too bad. It's not readable?

    Don't lie. It *IS* readable.
    """

    model: Optional[LightFM] = None
    dataset: Optional[Dataset] = None

    def build_dataset(self):
        # Build the dataset from the existing data (users, items)
        self.dataset = Dataset()
        self.dataset.fit(
            (user_id for user_id in User.objects.values_list('id', flat=True).order_by('id')),
            (product_id for product_id in Product.objects.values_list('id', flat=True).order_by('id')),
        )

    def build_model(self, epochs: int = 30):
        # Build the recommendation model
        self.model = LightFM(loss='warp')
        interactions_matrix, _ = self.dataset.build_interactions(
            ((user_id, product_id) for user_id, product_id in Heart.objects.values_list('user_id', 'product_id'))
        )
        self.model.fit(interactions_matrix, epochs=epochs)

    def recommend(self, user_id: int, num_recommendations: int = 6) -> list[int]:

        if not self.model or not self.dataset:
            self.build_dataset()
            self.build_model()

        already_liked_ids = Heart.objects.filter(user_id=user_id).values_list('product_id', flat=True)
        user_mapping, _, item_mapping, _ = self.dataset.mapping()
        user_internal_id = user_mapping[user_id]

        scores = self.model.predict(user_internal_id, list(item_mapping.values()))
        top_item_indices = np.argsort(-scores)

        top_items = [list(item_mapping.keys())[i] for i in top_item_indices]

        return [item for item in top_items if item not in already_liked_ids][:num_recommendations]
