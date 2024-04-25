import { createRouter, createWebHistory } from "vue-router";

import HomeView from "@/views/HomeView.vue";
import CartView from "@/views/CartView.vue";
import LoginView from "@/views/LoginView.vue";
import OrdersView from "@/views/OrdersView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
    },
    {
      path: "/login",
      name: "login",
      component: LoginView,
    },
    {
      path: "/cart",
      name: "cart",
      component: CartView,
    },
    {
      path: "/orders",
      name: "orders",
      component: OrdersView,
    },
  ],
});

export default router;
