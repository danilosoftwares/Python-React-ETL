export interface Product {
  id: number;
  name: string;
  price: number;
  expiration: string; 
  price_brl: number;
  price_cnh: number;
  price_mxn: number;
  price_pln: number;
  price_jpy: number;
}

export interface SortResponse {
  field:string;
  increasing:boolean;
}

export interface ProductResponse {
  data: Product[];
  total: number;
  sort:SortResponse;
}