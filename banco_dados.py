import sqlite3

def conectar():

    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()

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