<script setup lang="ts">
import { RouterLink } from "vue-router";
</script>

<template>
  <div class="container">
    <div class="alert alert-success" role="alert">
      <h4 class="alert-heading">Thank you for your order!</h4>
      <p>Your order has been placed successfully.</p>
      <hr />
      <p class="mb-0">
        You will receive an email confirmation shortly.
        <RouterLink :to="{ name: 'home' }">Continue shopping.</RouterLink>
      </p>
    </div>
  </div>
</template>
