export type Nullable<T> = T | null;

export type PaginatedResponse<T> = {
  results: T[];
  count: number;
  next: Nullable<string>;
  previous: Nullable<string>;
};
