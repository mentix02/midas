<script setup lang="ts">
import { ref, onMounted } from "vue";
import { fetchOrders } from "@/api/order";
import type { Order } from "@/api/types/order";
import type { PaginatedResponse } from "@/types";

const ordersResp = ref<PaginatedResponse<Order> | null>(null);

onMounted(async () => {
  ordersResp.value = await fetchOrders();
});
</script>

<template>
  <div class="container">
    <div class="text-center">
      <h1>Past Orders</h1>
    </div>
    <hr />
    <div class="row"></div>
  </div>
</template>
