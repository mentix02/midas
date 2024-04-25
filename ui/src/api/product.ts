import useAuthStore from "@/stores/auth";
import useTokenHeader from "@/api/headers";
import configureEndpoint from "@/api/host";
import type { PaginatedResponse } from "@/types";
import type { Product, ProductDetail } from "@/api/types/product";

const BASE_URL = configureEndpoint("api/v1/product");

export const fetchProductsResponse = async (page: number = 1): Promise<PaginatedResponse<Product>> => {
  const authStore = useAuthStore();

  const response = await fetch(`${BASE_URL}/?page=${page}`, {
    method: "GET",
    headers: authStore.isAuthenticated ? useTokenHeader() : {},
  });

  if (!response.ok) throw new Error("Failed to fetch products");

  return await response.json();
};

export const fetchProductDetails = async (productId: number): Promise<ProductDetail> => {
  const authStore = useAuthStore();

  const response = await fetch(`${BASE_URL}/${productId}/`, {
    method: "GET",
    headers: authStore.isAuthenticated ? useTokenHeader() : {},
  });

  if (!response.ok) throw new Error("Failed to fetch product details");

  return await response.json();
};
