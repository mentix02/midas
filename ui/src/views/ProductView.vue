<script setup lang="ts">
import { useRoute } from "vue-router";
import { ref, watch, onMounted } from "vue";

import { fetchProductDetails } from "@/api/product";
import type { ProductDetail } from "@/api/types/product";
import ProductCard from "@/components/product/ProductCard.vue";

const route = useRoute();

const product = ref<ProductDetail | null>(null);

watch(
  () => route.params.id,
  async (id) => {
    product.value = await fetchProductDetails(Number(id));
  }
);

onMounted(async () => {
  product.value = await fetchProductDetails(Number(route.params.id));
});
</script>

<template>
  <div v-if="product" class="container">
    <div class="row">
      <div class="col-12 col-lg-6">
        <ProductCard with-description :product="product" :height="600" />
      </div>
      <div class="col-12 col-lg-6">
        <h2>Users Also Bought</h2>
        <div class="row">
          <div
            class="col-6"
            :key="also_bought.id"
            v-if="product?.users_also_bought.length > 0"
            v-for="also_bought in product?.users_also_bought"
          >
            <ProductCard :product="also_bought" :height="200" />
          </div>
          <div v-else>
            <p>No products found. (try running <code>python3 manage.py generate_orders -n &lt;num_orders&gt;</code>)</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
