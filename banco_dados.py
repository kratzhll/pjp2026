import sqlite3

def conectar():

    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()

    # TABELA LIVROS
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS livros (

            livro_id INTEGER PRIMARY KEY AUTOINCREMENT,
            livro_nome VARCHAR(100) NOT NULL,
            categorias_id INT,
            editora_id INT,
            status_livro VARCHAR(50),
            autor VARCHAR(100),
            autor_id INTEGER,

            CONSTRAINT fk_livro_categoria
            FOREIGN KEY (categorias_id)
            REFERENCES categorias (categorias_id),

            CONSTRAINT fk_livro_editora
            FOREIGN KEY (editora_id)
            REFERENCES editora (editora_id)

        )
    """)

    # TABELA CATEGORIAS
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS categorias (

            categorias_id INTEGER PRIMARY KEY AUTOINCREMENT,
            categorias_nome VARCHAR(100) NOT NULL

        )
    """)

    # TABELA EMPRESTIMOS
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pedido_emprestimo (

            pedido_id INTEGER PRIMARY KEY AUTOINCREMENT,
            livro_id INT,
            cliente_id INT,
            status_livro VARCHAR(50),
            data_ped DATE,
            data_dev DATE,

            CONSTRAINT fk_pedido_livro
            FOREIGN KEY (livro_id)
            REFERENCES livros (livro_id),

            CONSTRAINT fk_pedido_cliente
            FOREIGN KEY (cliente_id)
            REFERENCES cliente (cliente_id)

        )
    """)

    # TABELA CLIENTE
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS cliente (

        cliente_id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_cliente VARCHAR(100) NOT NULL,
        cidade VARCHAR(50),
        email VARCHAR(100)

    )
""")


    conn.commit()

    return conn


# CADASTRAR LIVRO
def db_cadastrar_livro(livro_nome, autor):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO livros (livro_nome, autor) VALUES (?, ?)",
        (livro_nome, autor)
    )

    conn.commit()
    conn.close()


# LISTAR LIVROS
def db_listar_livros():

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM livros")

    dados = cursor.fetchall()

    conn.close()

    return dados


# DELETAR LIVRO
def db_deletar_livro(livro_id):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM livros WHERE livro_id = ?",
        (livro_id,)
    )

    conn.commit()
    conn.close()


# CADASTRAR CATEGORIAS
def db_cadastrar_categorias(categorias_nome):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO categorias (categorias_nome) VALUES (?)",
        (categorias_nome,)
    )

    conn.commit()
    conn.close()


# LISTAR CATEGORIAS
def db_listar_categorias():

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM categorias")

    dados = cursor.fetchall()

    conn.close()

    return dados


# DELETAR CATEGORIA
def db_deletar_categorias(categorias_id):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM categorias WHERE categorias_id = ?",
        (categorias_id,)
    )

    conn.commit()
    conn.close()

   # CADASTRAR EMPRESTIMOS
def db_cadastrar_emprestimos(
    livro_id,
    cliente_id,
    status_livro,
    data_ped,
    data_dev
):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO pedido_emprestimo (
            livro_id,
            cliente_id,
            status_livro,
            data_ped,
            data_dev
        )
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            livro_id,
            cliente_id,
            status_livro,
            data_ped,
            data_dev
        )
    )

    conn.commit()
    conn.close()


# LISTAR Empréstimos
def db_listar_emprestimos():

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM pedido_emprestimo")

    dados = cursor.fetchall()

    conn.close()

    return dados


# DELETAR Empréstimos
def db_deletar_emprestimos(pedido_id):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM pedido_emprestimo WHERE pedido_id = ?",
        (pedido_id,)
    )

    conn.commit()
    conn.close()

   # CADASTRAR CLIENTE
def db_cadastrar_cliente(nome_cliente, cidade, email):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO cliente (
            nome_cliente,
            cidade,
            email
        )
        VALUES (?, ?, ?)
        """,
        (nome_cliente, cidade, email)
    )

    conn.commit()
    conn.close()


# LISTAR CLIENTES
def db_listar_clientes():

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM cliente")

    dados = cursor.fetchall()

    conn.close()

    return dados


# DELETAR CLIENTE
def db_deletar_cliente(cliente_id):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM cliente WHERE cliente_id = ?",
        (cliente_id,)
    )

    conn.commit()
    conn.close()


# LISTAR cliente
def db_listar_clientes():

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM cliente")

    dados = cursor.fetchall()

    conn.close()

    return dados


# DELETAR cliente
def db_deletar_cliente(cliente_id):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM cliente WHERE cliente_id = ?",
        (cliente_id,)
    )

    conn.commit()
    conn.close()
