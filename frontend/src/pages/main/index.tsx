import React, { useCallback, useEffect, useRef, useState } from 'react';
import { DataTable, DataTableStateEvent } from 'primereact/datatable';
import { Column } from 'primereact/column';
import { Product } from '../../types/product';
import { fetchProducts } from '../../services/productService';
import { Paginator, PaginatorPageChangeEvent } from 'primereact/paginator';
import { FileUploadBeforeUploadEvent, FileUploadUploadEvent } from 'primereact/fileupload';
import { Progressing } from '../../components/progressing';
import { Toast } from 'primereact/toast';
import { Title } from '../../components/title';
import { NaviBar } from '../../components/navibar';

export const MainPage: React.FC = () => {
  const [products, setProducts] = useState<Product[]>([]);
  const [nameFilter, setNameFilter] = useState('');
  const [priceFilter, setPriceFilter] = useState<number | null | undefined>(undefined);
  const [expirationFilter, setExpirationFilter] = useState<Date | null | undefined>(undefined);
  const [sortingFilter, setSortingFilter] = useState<string | null | undefined>("id");
  const [total, setTotal] = useState(0);
  const [first, setFirst] = useState(0);
  const [rows, setRows] = useState(10);
  const [page, setPage] = useState(0);
  const [loading, setLoading] = useState(false);
  const [jobId, setJobId] = useState<string | undefined>(undefined);

  const toast = useRef<Toast>(null);

  const fetchData = useCallback(async (name: string, price: number | null | undefined, expiration: Date | null | undefined, sort: string | null | undefined, page: number, rows: number) => {
    const response = await fetchProducts({ name: name, price: price, expiration: expiration, sort: sort, page: page, limit: rows });
    setProducts(response.data);
    setTotal(response.total);
  }, []);

  const onUpload = (event: FileUploadUploadEvent) => {
    const uploadResponse = JSON.parse(event.xhr.response);
    setJobId(uploadResponse.job);
  };

  const beforeUpload = (event: FileUploadBeforeUploadEvent) => {
    setLoading(true);
  }

  const onPageChange = (event: PaginatorPageChangeEvent) => {
    setFirst(event.first);
    setRows(event.rows);
    setPage(event.page);
  };

  const search = async () => {
    fetchData(nameFilter, priceFilter, expirationFilter, sortingFilter, page, rows);
  }

  const sorting = async (event: DataTableStateEvent) => {
    setSortingFilter(`${event.sortOrder === -1 ? "-" : ""}${event.sortField}`)
  }

  const onFilter = (name: string, price: number | null | undefined, expiration: Date | null | undefined) => {
    setNameFilter(name);
    setPriceFilter(price);
    setExpirationFilter(expiration);
  }

  const finishProgress = () => {
    setJobId(undefined);
    setLoading(false);
    search();
    setTimeout(() => {
      if (toast && toast.current) {
        toast.current.show({ severity: 'success', summary: 'Success', detail: 'Data imported successfully' });
      }
    }, 1000);
  }

  useEffect(() => {
    fetchData(nameFilter, priceFilter, expirationFilter, sortingFilter, page, rows);
    // eslint-disable-next-line
  }, [fetchData, page, rows, sortingFilter]);

  return (
    <div style={{ display: 'flex', flexDirection: 'column', margin: '50px 10% 0px 10%', height: '90vh', justifyContent: "flex-start" }}>
      <Toast ref={toast} />
      {loading ? <Progressing onFinish={finishProgress} jobId={jobId} /> :
        <div>
          <Title text={"Price Products"} />
          <NaviBar nameFilter={nameFilter} priceFilter={priceFilter} expirationFilter={expirationFilter} onFilter={onFilter} search={search} beforeUpload={beforeUpload} onUpload={onUpload} />

          <DataTable value={products} rows={rows} scrollable height={"65vh"} scrollHeight="65vh" loading={loading} sortField={sortingFilter ? sortingFilter.replace('-', '') : ''} sortOrder={sortingFilter ? sortingFilter?.indexOf('-') > -1 ? -1 : 1 : 1} onSort={sorting} >
            <Column field="id" header="ID" sortable />
            <Column field="name" header="Nome" sortable />
            <Column field="price" header="Price" headerStyle={{ textAlign: 'right' }} bodyStyle={{ textAlign: 'right' }} sortable />
            <Column field="expiration" header="Expiration" sortable />
            <Column field="price_brl" header="In Brazil" headerStyle={{ textAlign: 'right' }} bodyStyle={{ textAlign: 'right', paddingRight: '60px' }} />
            <Column field="price_cnh" header="In China" headerStyle={{ textAlign: 'right' }} bodyStyle={{ textAlign: 'right', paddingRight: '60px' }} />
            <Column field="price_mxn" header="In Mexico" headerStyle={{ textAlign: 'right' }} bodyStyle={{ textAlign: 'right', paddingRight: '60px' }} />
            <Column field="price_pln" header="In Poland" headerStyle={{ textAlign: 'right' }} bodyStyle={{ textAlign: 'right', paddingRight: '60px' }} />
            <Column field="price_jpy" header="In Japan" headerStyle={{ textAlign: 'right' }} bodyStyle={{ textAlign: 'right', paddingRight: '60px' }} />
          </DataTable>
          <Paginator first={first} rows={rows} totalRecords={total} rowsPerPageOptions={[10, 20, 30]} onPageChange={onPageChange} />
        </div>}
    </div>
  );

};

