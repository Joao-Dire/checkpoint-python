import oracledb

def get_conexao():
    return oracledb.connect(user="RM554749", password="290704",
                            dsn="oracle.fiap.com.br/orcl")

def converte(registro):
    return {
        'id': registro[0],
        'titulo': registro[1],
        'descricao': registro[2],
        'preco': registro[3],
        'data_inicio': registro[4],
        'duracao_horas': registro[5]
    }

def consulta_todos():
    sql = "SELECT * FROM curso_online"
    lista = []
    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(sql)
            dados = cur.fetchall()
            for reg in dados:
                lista.append(converte(reg))
    return lista

def consulta_id(id):
    sql = "SELECT id, titulo, descricao, preco, data_inicio, duracao_horas FROM curso_online WHERE id=:id"
    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(sql, {"id": id})
            dado = cur.fetchone()
            return converte(dado) if dado else None

def insere(curso):
    sql = """
        INSERT INTO curso_online (titulo, descricao, preco, data_inicio, duracao_horas)
        VALUES (:titulo, :descricao, :preco, TO_DATE(:data_inicio, 'YYYY-MM-DD'), :duracao_horas) 
        RETURNING id INTO :id
    """
    with get_conexao() as con:
        with con.cursor() as cur:
            novo_id = cur.var(oracledb.NUMBER)
            curso['id'] = novo_id
            cur.execute(sql, curso)
        con.commit()
        curso['id'] = novo_id.getvalue()[0]

def altera(curso):
    sql = """
        UPDATE curso_online 
        SET titulo=:titulo, descricao=:descricao, preco=:preco, 
            data_inicio=TO_DATE(:data_inicio, 'YYYY-MM-DD'), duracao_horas=:duracao_horas 
        WHERE id=:id
    """
    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(sql, curso)
        con.commit()

def exclui(id):
    sql = "DELETE FROM curso_online WHERE id=:id"
    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(sql, {"id": id})
        con.commit()
