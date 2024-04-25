<script setup lang="ts">
import { ref, computed, onMounted } from "vue";
import { useRouter, RouterLink } from "vue-router";

import { checkout } from "@/api/order";
import useAuthStore from "@/stores/auth";
import type { Cart, CartItem } from "@/api/types/cart";
import { fetchCart, deleteFromCart } from "@/api/cart";

const router = useRouter();
const authStore = useAuthStore();
const cart = ref<Cart | null>(null);

const getCart = async () => (cart.value = await fetchCart());

const handleCheckout = async () => {
  try {
    await checkout();
    await router.push({ name: "checkout" });
  } catch (err: any) {
    alert(`Failed to checkout: ${err.message}`);
  }
};

const totalCost = computed(() => {
  if (!cart.value) return 0;

  return cart.value.results.reduce((acc: number, item: CartItem) => {
    return acc + Number(item.product.price) * item.quantity;
  }, 0);
});

const handleDelete = async (cartItemId: number) => {
  await deleteFromCart(cartItemId);
  await getCart();
};

onMounted(async () => {
  await getCart();
});
</script>

<template>
  <div class="container">
    <h1 class="text-center">{{ authStore.username }}'s Cart</h1>
    <hr />
    <div class="row justify-content-center">
      <div class="col-8">
        <table class="table table-hover">
          <thead>
            <tr>
              <th>Product</th>
              <th>Price</th>
              <th>Quantity</th>
              <th>Total</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <template v-if="cart && cart.count !== 0">
              <tr v-for="item in cart.results" :key="item.id">
                <td>
                  <RouterLink :to="{ name: 'product', params: { id: item.product.id } }">
                    {{ item.product.name }}
                  </RouterLink>
                </td>
                <td>${{ item.product.price }}</td>
                <td>&times; {{ item.quantity }}</td>
                <td>${{ Number(item.product.price) * item.quantity }}</td>
                <td>
                  <button class="btn btn-danger" @click="handleDelete(item.id)">
                    <i class="bi bi-trash"></i>
                  </button>
                </td>
              </tr>
              <tr>
                <td colspan="3" class="text-end">Total</td>
                <td>${{ totalCost }}</td>
                <td></td>
              </tr>
            </template>
            <template v-else>
              <tr>
                <td colspan="5" class="text-center">
                  No items in cart. <RouterLink :to="{ name: 'home' }">Continue shopping</RouterLink>!
                </td>
              </tr>
            </template>
          </tbody>
        </table>

        <div class="text-center">
          <button v-if="cart && cart.count !== 0" @click="handleCheckout" class="btn btn-primary">Checkout</button>
        </div>
      </div>
    </div>
  </div>
</template>
