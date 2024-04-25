import configureEndpoint from "@/api/host";
import type { PaginatedResponse } from "@/types";
import type { Product } from "@/api/types/product";

const BASE_URL = configureEndpoint("api/v1/product");

export const fetchProductsResponse = async (page: number = 1): Promise<PaginatedResponse<Product>> => {
  const response = await fetch(`${BASE_URL}/?page=${page}`);

  if (!response.ok) throw new Error("Failed to fetch products");

  return await response.json();
};
