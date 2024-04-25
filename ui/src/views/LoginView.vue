<script setup lang="ts">
import { ref } from "vue";
import { useRouter } from "vue-router";

import { login } from "@/api/auth";
import useAuthStore from "@/stores/auth";
import type { Credentials } from "@/api/types/auth";

const router = useRouter();
const authStore = useAuthStore();
const credentials = ref<Credentials>({ username: "", password: "" });

const handleLogin = async () => {
  try {
    const tokenResp = await login(credentials.value);
    authStore.login(tokenResp, credentials.value.username);
    await router.push({ name: "home" });
  } catch (err: any) {
    alert(err.message);
  }
};
</script>

<template>
  <div class="container">
    <div class="row justify-content-center">
      <div class="col-6">
        <h1 class="text-center">Welcome Back</h1>
        <hr />
        <form @submit.prevent="handleLogin">
          <div class="mb-3">
            <label for="username" class="form-label">Username</label>
            <input autofocus type="text" id="username" class="form-control" v-model="credentials.username" />
          </div>
          <div class="mb-3">
            <label for="password" class="form-label">Password</label>
            <input v-model="credentials.password" type="password" class="form-control" id="password" />
            <div class="form-text">Check out README.md for a list of credentials to sign in</div>
          </div>
          <button type="submit" class="btn btn-primary">Submit</button>
        </form>
      </div>
    </div>
  </div>
</template>
