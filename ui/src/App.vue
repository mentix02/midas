<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({ name: "Midas" });
</script>

<script setup lang="ts">
import { RouterView } from "vue-router";

import Navigation from "@/components/layout/Navigation.vue";
</script>

<template>
  <Navigation />
  <router-view />
</template>
