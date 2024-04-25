<script setup lang="ts">
import { RouterLink } from "vue-router";
import { ref, computed, onMounted } from "vue";

import type { Cart } from "@/api/types/cart";
import { fetchCart, deleteFromCart } from "@/api/cart";

const cart = ref<Cart | null>(null);

const getCart = async () => {
  cart.value = await fetchCart();
};

const totalCost = computed(() => {
  if (!cart.value) return 0;

  return cart.value.results.reduce((acc, item) => {
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
    <h1 class="text-center">Cart</h1>
    <hr />
    <div class="row justify-content-center">
      <div class="col-8">
        <table class="table">
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
                <td>{{ item.product.name }}</td>
                <td>${{ item.product.price }}</td>
                <td>&times; {{ item.quantity }}</td>
                <td>${{ Number(item.product.price) * item.quantity }}</td>
                <td>
                  <button class="btn btn-danger" @click="handleDelete(item.id)">Remove</button>
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
          <RouterLink v-if="cart && cart.count !== 0" to="/" class="btn btn-primary"> Checkout </RouterLink>
        </div>
      </div>
    </div>
  </div>
</template>
