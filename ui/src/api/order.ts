import { fetchCart } from "@/api/cart";
import useTokenHeader from "@/api/headers";
import configureEndpoint from "@/api/host";
import type { Order } from "@/api/types/order";
import type { PaginatedResponse } from "@/types";

const BASE_URL = configureEndpoint("api/v1/order");

export const checkout = async (): Promise<boolean> => {
  // check cart contains items
  const cart = await fetchCart();
  if (cart.count === 0) throw new Error("Cart is empty");

  const resp = await fetch(`${BASE_URL}/checkout/`, { method: "POST", headers: useTokenHeader() });

  if (!resp.ok) throw new Error("Failed to checkout");

  return true;
};

export const fetchOrders = async (page: number = 1): Promise<PaginatedResponse<Order>> => {
  const resp = await fetch(`${BASE_URL}/?page=${page}`, { headers: useTokenHeader() });

  if (!resp.ok) throw new Error("Failed to fetch orders");

  return await resp.json();
};
