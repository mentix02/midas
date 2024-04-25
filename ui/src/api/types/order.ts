import type { Product } from "@/api/types/product";

export type OrderItem = {
  readonly id: number;
  readonly product: Product;
  readonly quantity: number;
};

export type Order = {
  readonly id: number;
  readonly total: number;
  readonly timestamp: string;
  readonly items: OrderItem[];
};
