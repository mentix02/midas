import { createRouter, createWebHistory } from "vue-router";

import HomeView from "@/views/HomeView.vue";
import CartView from "@/views/CartView.vue";
import LoginView from "@/views/LoginView.vue";
import HeartsView from "@/views/HeartsView.vue";
import OrdersView from "@/views/OrdersView.vue";
import ProductView from "@/views/ProductView.vue";
import CheckoutView from "@/views/CheckoutView.vue";
import RecommendationsView from "@/views/RecommendationsView.vue";

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
    {
      path: "/hearts",
      name: "hearts",
      component: HeartsView,
    },
    {
      path: "/product/:id",
      name: "product",
      component: ProductView,
    },
    {
      path: "/checkout",
      name: "checkout",
      component: CheckoutView,
    },
    {
      path: "/recommendations",
      name: "recommendations",
      component: RecommendationsView,
    },
  ],
});

export default router;
