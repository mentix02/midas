<script setup lang="ts">
import { useRouter, RouterLink } from "vue-router";

import { addToCart } from "@/api/cart";
import useAuthStore from "@/stores/auth";
import { toggleHeart } from "@/api/heart";
import type { Product } from "@/api/types/product";

const router = useRouter();
const authStore = useAuthStore();

interface ProductCardProps {
  height?: number;
  product: Product;
  withDescription?: boolean;
}

const props = withDefaults(defineProps<ProductCardProps>(), { height: 400, withDescription: false });

const handleToggleHeart = async () => {
  if (!authStore.isAuthenticated) {
    alert("Sign in to heart items.");
    return;
  }
  try {
    await toggleHeart(props.product.id);
  } catch (err: any) {
    alert(`Failed to heart item: ${err.message}`);
  }
  props.product.is_hearted = !props.product.is_hearted;
};

const handleAddToCart = async () => {
  if (!authStore.isAuthenticated) {
    alert("Sign in to add items to cart.");
    return;
  }
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
      <p v-if="withDescription" class="card-text">{{ product.description }}</p>
      <p class="card-text">${{ product.price }}</p>
      <div class="btn-group" role="group" v-if="authStore.isAuthenticated">
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
