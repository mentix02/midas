<script setup lang="ts">
import { ref, onMounted } from "vue";

import type { PaginatedResponse } from "@/types";
import type { Product } from "@/api/types/product";
import { fetchHeartedProducts } from "@/api/heart";
import ProductCard from "@/components/product/ProductCard.vue";

const page = ref<number>(1);
const heartedProductsResponse = ref<PaginatedResponse<Product> | null>(null);

const loadMore = async () => {
  const response = await fetchHeartedProducts(page.value + 1);
  heartedProductsResponse.value = {
    ...response,
    results: [...heartedProductsResponse.value!.results, ...response.results],
  };
  page.value++;
};

onMounted(async () => {
  heartedProductsResponse.value = await fetchHeartedProducts();
});
</script>

<template>
  <div class="container">
    <div class="row">
      <div class="col-12 col-lg-4" v-for="product in heartedProductsResponse?.results" :key="product.id">
        <ProductCard :product="product" />
      </div>
    </div>
  </div>
</template>
