import type { PaginatedResponse } from "@/types";
import type { Product } from "@/api/types/product";

export type CartItem = {
  quantity: number;
  readonly id: number;
  readonly product: Product;
};

export type Cart = PaginatedResponse<CartItem>;
