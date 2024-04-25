<script setup lang="ts">
import { ref } from "vue";
import { RouterLink, useRouter } from "vue-router";

import useAuthStore from "@/stores/auth";

const router = useRouter();
const authStore = useAuthStore();
const navbarOpen = ref<boolean>(false);

const toggleNavbar = () => (navbarOpen.value = !navbarOpen.value);

const handleLogout = async () => {
  authStore.logout();
  await router.push({ name: "login" });
};
</script>

<template>
  <nav class="navbar navbar-expand-lg bg-primary mb-4" data-bs-theme="dark">
    <div class="container">
      <RouterLink class="navbar-brand" :to="{ name: 'home' }">Midas</RouterLink>
      <button
        type="button"
        @click="toggleNavbar"
        class="navbar-toggler"
        :aria-expanded="navbarOpen"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div :class="{ show: navbarOpen }" class="collapse navbar-collapse justify-content-end">
        <ul class="navbar-nav">
          <li class="nav-item">
            <RouterLink class="nav-link" :to="{ name: 'home' }" active-class="active">Home</RouterLink>
          </li>
          <template v-if="!authStore.isAuthenticated">
            <li class="nav-item">
              <RouterLink class="nav-link" :to="{ name: 'login' }" active-class="active">Login</RouterLink>
            </li>
          </template>
          <template v-else>
            <li class="nav-item">
              <RouterLink class="nav-link" :to="{ name: 'cart' }" active-class="active">Cart</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" :to="{ name: 'orders' }" active-class="active">Orders</RouterLink>
            </li>
            <li class="nav-item pointer" @click="handleLogout">
              <span class="nav-link">Logout</span>
            </li>
          </template>
        </ul>
      </div>
    </div>
  </nav>
</template>

<style>
.pointer {
  cursor: pointer;
}
</style>
