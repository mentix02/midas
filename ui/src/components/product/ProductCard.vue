<script setup lang="ts">
import { useRouter, RouterLink } from "vue-router";

import { addToCart } from "@/api/cart";
import { toggleHeart } from "@/api/heart";
import type { Product } from "@/api/types/product";

const router = useRouter();

const props = withDefaults(defineProps<{ product: Product; height?: number }>(), {
  height: 400,
});

const handleToggleHeart = async () => {
  try {
    await toggleHeart(props.product.id);
  } catch (err: any) {
    alert(`Failed to heart item: ${err.message}`);
  }
  props.product.is_hearted = !props.product.is_hearted;
};

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
    <RouterLink :to="{ name: 'product', params: { id: product.id } }">
      <img :height="height" :src="product.image" class="card-img-top" :alt="product.name" />
    </RouterLink>
    <div class="card-body">
      <h5 class="card-title">{{ product.name }}</h5>
      <p class="card-text">{{ product.description }}</p>
      <p class="card-text">${{ product.price }}</p>
      <div class="btn-group" role="group">
        <button @click="handleAddToCart" class="btn btn-primary">
          <i class="bi bi-cart-plus"></i>
        </button>
        <button @click="handleToggleHeart" class="btn" :class="{ 'btn-danger': Boolean(product.is_hearted) }">
          <i v-if="product.is_hearted" class="bi bi-heart-fill"></i>
          <i v-else class="bi bi-heart"></i>
        </button>
      </div>
    </div>
  </div>
</template>
