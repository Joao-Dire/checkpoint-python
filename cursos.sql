CREATE TABLE curso_online (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    descricao TEXT NOT NULL,
    preco FLOAT NOT NULL,
    data_inicio DATE NOT NULL,
    duracao_horas INT NOT NULL
);
