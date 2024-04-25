import type { Nullable } from "@/types";

export type Product = {
  readonly id: number;
  readonly name: string;
  readonly image: string;
  readonly price: string;
  readonly description: string;
  readonly is_hearted?: Nullable<boolean>;
};
