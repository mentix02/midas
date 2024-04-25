import useTokenHeader from "@/api/headers";
import configureEndpoint from "@/api/host";
import type { Cart } from "@/api/types/cart";

const BASE_URL = configureEndpoint("api/v1/cart");

export const fetchCart = async (): Promise<Cart> => {
  const response = await fetch(`${BASE_URL}/`, { headers: useTokenHeader() });

  if (!response.ok) throw new Error("Failed to fetch cart");

  return await response.json();
};

export const addToCart = async (productId: number, quantity: number = 1): Promise<boolean> => {
  const formData = new FormData();

  formData.set("product", String(productId));
  formData.set("quantity", quantity.toString());

  const response = await fetch(`${BASE_URL}/`, {
    method: "POST",
    body: formData,
    headers: useTokenHeader(),
  });

  if (!response.ok) throw new Error("Failed to add to cart");

  return true;
};

export const deleteFromCart = async (cartItemId: number): Promise<boolean> => {
  const response = await fetch(`${BASE_URL}/${cartItemId}/`, {
    method: "DELETE",
    headers: useTokenHeader(),
  });

  if (!response.ok) throw new Error("Failed to delete from cart");

  return true;
};
