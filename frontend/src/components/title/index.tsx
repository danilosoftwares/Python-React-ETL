import React from 'react';

interface TitleProps {
    text: string;
}

export const Title: React.FC<TitleProps> = ({ text }) => {

    return (
        <h3 style={{ color: "#2563eb", display: "flex", fontSize: "xx-large", margin: "0px 0px 35px 0px", borderBottom: "1px solid #2563eb" }}>{text}</h3>
    );
};

