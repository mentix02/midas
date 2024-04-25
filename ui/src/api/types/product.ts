import type { Nullable } from "@/types";

export type Product = {
  readonly id: number;
  readonly name: string;
  readonly image: string;
  readonly price: string;
  readonly description: string;
  is_hearted?: Nullable<boolean>;
};

export type ProductDetail = {
  readonly id: number;
  readonly name: string;
  readonly image: string;
  readonly price: string;
  readonly description: string;
  is_hearted?: Nullable<boolean>;
  readonly users_also_bought: Product[];
};
