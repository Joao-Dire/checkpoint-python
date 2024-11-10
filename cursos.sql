CREATE TABLE curso_online (
    id NUMBER GENERATED BY DEFAULT ON NULL AS IDENTITY PRIMARY KEY,
    titulo VARCHAR2(255) NOT NULL,
    descricao CLOB NOT NULL,
    preco NUMBER(10, 2) NOT NULL,
    data_inicio DATE NOT NULL,
    duracao_horas NUMBER NOT NULL
);
