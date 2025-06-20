import { Button } from 'primereact/button';
import { Calendar } from 'primereact/calendar';
import { FileUpload, FileUploadBeforeUploadEvent, FileUploadUploadEvent } from 'primereact/fileupload';
import { FloatLabel } from 'primereact/floatlabel';
import { InputNumber } from 'primereact/inputnumber';
import { InputText } from 'primereact/inputtext';
import React from 'react';
import api from '../../services/baseService';

interface NaviBarProps {
    nameFilter: string;
    priceFilter: number | null | undefined;
    expirationFilter: Date | null | undefined;
    onFilter: (name: string, price: number | null | undefined, expiration: Date | null | undefined) => void;
    search: React.MouseEventHandler<HTMLButtonElement> | undefined;
    beforeUpload: (event: FileUploadBeforeUploadEvent) => void;
    onUpload: (event: FileUploadUploadEvent) => void;
}

export const NaviBar: React.FC<NaviBarProps> = ({ nameFilter, priceFilter, expirationFilter, onFilter, search, beforeUpload, onUpload }) => {

    return (
        <div style={{ gap: '1rem', display: 'flex', justifyContent: 'space-between', margin: '15px 0px' }}>
            <div style={{ gap: '1rem', display: 'flex' }}>
                <span className="p-float-label">
                    <InputText
                        id="nameFilter"
                        value={nameFilter}
                        onChange={(e) => onFilter(e.target.value, priceFilter, expirationFilter)}
                    />
                    <label htmlFor="nameFilter">Name</label>
                </span>

                <span className="p-float-label">
                    <InputNumber
                        minFractionDigits={2} maxFractionDigits={5}
                        id="price"
                        value={priceFilter}
                        onValueChange={(e) => onFilter(nameFilter, e.target.value, expirationFilter)}
                    />
                    <label htmlFor="price">Price</label>
                </span>


                <FloatLabel>
                    <Calendar inputId="expiration" value={expirationFilter} onChange={(e) => onFilter(nameFilter, priceFilter, e.value)} dateFormat='yy-mm-dd' />
                    <label htmlFor="expiration">Expiration</label>
                </FloatLabel>

                <span className="p-float-label">
                    <Button
                        label='Search'
                        icon="pi pi-search"
                        onClick={search}
                    />
                </span>
            </div>
            <span className="p-float-label">
                <FileUpload mode="basic" name="file" url={`${api.getUri()}/products/Upload`} accept="csv/*" onUpload={onUpload} onBeforeUpload={beforeUpload} />
            </span>
        </div>

    );
};

