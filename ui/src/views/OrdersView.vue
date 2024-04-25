<script setup lang="ts">
import { ref, onMounted } from "vue";
import { RouterLink } from "vue-router";

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
    <br /><br />
    <div class="row">
      <div class="col-12">
        <div v-if="ordersResp && ordersResp.results.length > 0">
          <div v-for="order in ordersResp?.results" :key="order.id">
            <h3>Order #{{ order.id }}</h3>
            <hr />
            <table class="table table-hover">
              <thead>
                <tr>
                  <th>Item ID</th>
                  <th>Product</th>
                  <th>Price</th>
                  <th>Quantity</th>
                  <th>Total</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="orderItem in order.items" :key="orderItem.id">
                  <td>{{ orderItem.id }}</td>
                  <td>
                    <RouterLink :to="{ name: 'product', params: { id: orderItem.product.id } }">{{
                      orderItem.product.name
                    }}</RouterLink>
                  </td>
                  <td>${{ orderItem.product.price }}</td>
                  <td>&times;{{ orderItem.quantity }}</td>
                  <td>${{ Number(orderItem.product.price) * orderItem.quantity }}</td>
                </tr>
              </tbody>
            </table>
            <br /><br />
          </div>
        </div>
        <div v-else>
          <p>No orders found.</p>
        </div>
      </div>
    </div>
  </div>
</template>
