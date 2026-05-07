import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# --- BANCO DE DADOS ---
def conectar():
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS livros (
            livro_id INTEGER PRIMARY KEY AUTOINCREMENT, 
            livro_nome VARCHAR(100) NOT NULL
        )
    """)
    conn.commit()
    return conn


# --- LÓGICA DAS TELAS ---

def obter_categorias():
    """Retorna uma lista de tuplas (id, nome) das categorias."""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT categorias_id, categorias_nome FROM categorias")
    dados = cursor.fetchall()
    conn.close()
    return dados

def obter_editoras():
    """Retorna uma lista de tuplas (id, nome) das categorias."""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT editora_id, editora_nome FROM categorias")
    dados = cursor.fetchall()
    conn.close()
    return dados

 
def abrir_cadastro_livro(parent, livro_id=None):
    janela_cad = tk.Toplevel(parent)
    janela_cad.title("Editar Livro" if livro_id else "Cadastrar Livro")
    janela_cad.geometry("350x200")

    # Campo: Seleção de Categoria (Combobox)
    tk.Label(janela_cad, text="Selecione a Categoria:").pack(pady=(15, 5))
   
    # Buscamos as categorias do banco
    lista_categorias = obter_categorias() # Formato: [(1, 'Eletrônicos'), (2, 'Móveis')]
   
    # Criamos uma lista apenas com os nomes para exibir no Combobox
    nomes_categorias = [c[1] for c in lista_categorias]
   
    combo_categoria = ttk.Combobox(janela_cad, values=nomes_categorias, width=32, state="readonly")
    combo_categoria.pack()
    
    tk.Label(janela_cad, text="Nome do Livro:", font=("Arial", 10)).pack(pady=10)
    ent_nome = tk.Entry(janela_cad, width=30)
    ent_nome.pack(pady=5)

    if livro_id:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT livro_nome FROM livros WHERE livro_id = ?", 
            (livro_id,)
        )
        resultado = cursor.fetchone()
        if resultado:
            ent_nome.insert(0, resultado[0])
        conn.close()
    
    def salvar():
        nome = ent_nome.get()

        if not nome.strip():
            messagebox.showwarning("Aviso", "O nome não pode estar vazio.")
            return

        conn = conectar()
        cursor = conn.cursor()
        
        if livro_id:
            cursor.execute(
                "UPDATE livros SET livro_nome = ? WHERE livro_id = ?", 
                (nome, livro_id)
            )
            mensagem = "Livro atualizado com sucesso!"
        else:
            cursor.execute(
                "INSERT INTO livros (livro_nome) VALUES (?)", 
                (nome,)
            )
            mensagem = "Livro cadastrado com sucesso!"
            
        conn.commit()
        conn.close()
        messagebox.showinfo("Sucesso", mensagem)
        janela_cad.destroy()

    btn_texto = "Atualizar" if livro_id else "Cadastrar"
    btn_cor = "#ffcc00" if livro_id else "lightgreen"
    
    tk.Button(janela_cad, text=btn_texto, command=salvar, bg=btn_cor).pack(pady=20)


def abrir_consulta_livros(parent):
    janela_con = tk.Toplevel(parent)
    janela_con.title("Consultar Livros")
    janela_con.geometry("500x480") 

    colunas = ("ID", "Nome do Livro")
    tabela = ttk.Treeview(janela_con, columns=colunas, show="headings")
    tabela.heading("ID", text="ID")
    tabela.heading("Nome do Livro", text="Nome do Livro")
    tabela.column("ID", width=50, anchor="center")
    tabela.pack(pady=20, padx=10, fill="both", expand=True)

    def executar_edicao():
        item = tabela.selection()

        if not item:
            messagebox.showwarning("Aviso", "Selecione um livro!")
            return

        valores = tabela.item(item, "values")
        liv_id = int(valores[0])

        abrir_cadastro_livro(parent, livro_id=liv_id)
        janela_con.destroy()

    frame_botoes = tk.Frame(janela_con)
    frame_botoes.pack(pady=10)

    tk.Button(
        frame_botoes, 
        text="Editar Selecionado", 
        command=executar_edicao,
        bg="#ffcc00",
        font=("Arial", 10, "bold"),
        width=20
    ).pack(side="left", padx=5)

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM livros")
    
    for linha in cursor.fetchall():
        tabela.insert("", tk.END, values=linha)
    
    conn.close()