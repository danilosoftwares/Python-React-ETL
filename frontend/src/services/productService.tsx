import { ProductResponse } from '../types/product';
import api from './baseService';

interface FilterParams {
  page: number;
  limit: number;
  name?: string;
  price?: number | null | undefined;
  expiration?: Date | null | undefined;
  sort?: string | null | undefined;
}

export const fetchProducts = async (filters: FilterParams): Promise<ProductResponse> => {
  let query = "";
  query += filters.name ? '&name=' + filters.name : '';
  query += filters.expiration ? '&expiration=' + filters.expiration.toJSON().substring(0, filters.expiration.toJSON().indexOf('T')) : '';
  query += filters.price !== null && filters.price !== undefined ? '&price=' + filters.price : '';
  query += filters.sort ? '&sort=' + filters.sort : '';
  const response = await api.get<ProductResponse>(`/products/All?skip=${filters.page}&limit=${filters.limit}${query}`);
  return response.data;
};
