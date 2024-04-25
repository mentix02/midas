<script setup lang="ts">
import { ref, onMounted } from "vue";

import type { PaginatedResponse } from "@/types";
import type { Product } from "@/api/types/product";
import { fetchRecommendedProducts } from "@/api/heart";
import ProductCard from "@/components/product/ProductCard.vue";

const page = ref<number>(1);
const recommendedProductsResponse = ref<PaginatedResponse<Product> | null>(null);

const loadMore = async () => {
  const response = await fetchRecommendedProducts(page.value + 1);
  recommendedProductsResponse.value = {
    ...response,
    results: [...recommendedProductsResponse.value!.results, ...response.results],
  };
  page.value++;
};

onMounted(async () => {
  recommendedProductsResponse.value = await fetchRecommendedProducts();
});
</script>

<template>
  <div class="container">
    <div class="row">
      <div class="col-12 col-lg-4" v-for="product in recommendedProductsResponse?.results" :key="product.id">
        <ProductCard :product="product" />
      </div>
    </div>
  </div>
</template>
