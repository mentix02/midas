import useTokenHeader from "@/api/headers";
import configureEndpoint from "@/api/host";
import type { PaginatedResponse } from "@/types";
import type { Product } from "@/api/types/product";
import type { ToggleHeartResponse } from "@/api/types/heart";

const BASE_URL = configureEndpoint("api/v1/heart");

export const toggleHeart = async (productId: number): Promise<boolean> => {
  const formData = new FormData();

  formData.set("product_id", String(productId));

  const response = await fetch(`${BASE_URL}/toggle/`, {
    method: "POST",
    body: formData,
    headers: useTokenHeader(),
  });

  if (!response.ok) throw new Error("Failed to toggle heart");

  const respData: ToggleHeartResponse = await response.json();
  return respData.result;
};

export const fetchHeartedProducts = async (page: number = 1): Promise<PaginatedResponse<Product>> => {
  const response = await fetch(`${BASE_URL}/hearted/?page=${page}`, { headers: useTokenHeader() });

  if (!response.ok) throw new Error("Failed to fetch hearted products");

  return (await response.json()) as PaginatedResponse<Product>;
};

export const fetchRecommendedProducts = async (page: number = 1): Promise<PaginatedResponse<Product>> => {
  const response = await fetch(`${BASE_URL}/recommended/?page=${page}`, { headers: useTokenHeader() });

  if (!response.ok) throw new Error("Failed to fetch recommended products");

  return (await response.json()) as PaginatedResponse<Product>;
};
