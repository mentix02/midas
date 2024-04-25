<script setup lang="ts">
import { useRouter } from "vue-router";

import { addToCart } from "@/api/cart";
import type { Product } from "@/api/types/product";

const router = useRouter();

const props = defineProps<{
  product: Product;
}>();

const handleAddToCart = async () => {
  try {
    await addToCart(props.product.id);
  } catch (err: any) {
    alert(`Failed to add to cart: ${err.message}`);
  }
  await router.push({ name: "cart" });
};
</script>

<template>
  <div class="card">
    <img height="400" :src="product.image" class="card-img-top" :alt="product.name" />
    <div class="card-body">
      <h5 class="card-title">{{ product.name }}</h5>
      <p class="card-text">{{ product.description }}</p>
      <p class="card-text">${{ product.price }}</p>
      <button @click="handleAddToCart" class="btn btn-primary">Add to cart</button>
    </div>
  </div>
</template>
