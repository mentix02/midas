<script setup lang="ts">
import { ref, onMounted } from "vue";

import type { PaginatedResponse } from "@/types";
import type { Product } from "@/api/types/product";
import { fetchProductsResponse } from "@/api/product";
import ProductCard from "@/components/product/ProductCard.vue";

const page = ref<number>(1);
const productsResp = ref<PaginatedResponse<Product> | null>(null);

const loadMore = async () => {
  const response = await fetchProductsResponse(page.value + 1);
  productsResp.value = {
    ...response,
    results: [...productsResp.value!.results, ...response.results],
  };
  page.value++;
};

onMounted(async () => {
  productsResp.value = await fetchProductsResponse();
});
</script>

<template>
  <div class="container">
    <div class="row g-4">
      <div class="col-12 col-lg-4" v-for="product in productsResp?.results" :key="product.id">
        <ProductCard :product="product" />
      </div>
    </div>
    <div class="row justify-content-center">
      <div class="col-12 text-center">
        <br />
        <button v-if="productsResp?.next" @click="loadMore" class="btn btn-primary">Load more</button>
        <br />
        <br />
      </div>
    </div>
  </div>
</template>
