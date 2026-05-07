import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# --- BANCO DE DADOS ---
def conectar():
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS autor (
            autor_id INTEGER PRIMARY KEY AUTOINCREMENT, 
            nome_autor VARCHAR(100) NOT NULL
        )
    """)
    conn.commit()
    return conn


# --- LÓGICA DAS TELAS ---

def abrir_cadastro_autor(parent, autor_id=None):
    janela_cad = tk.Toplevel(parent)
    janela_cad.title("Editar Autor" if autor_id else "Cadastrar Autor")
    janela_cad.geometry("350x200")
    
    tk.Label(janela_cad, text="Nome do Autor:", font=("Arial", 10)).pack(pady=10)
    ent_nome = tk.Entry(janela_cad, width=30)
    ent_nome.pack(pady=5)

    if autor_id:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT nome_autor FROM autor WHERE autor_id = ?", 
            (autor_id,)
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
        
        if autor_id:
            cursor.execute(
                "UPDATE autor SET nome_autor = ? WHERE autor_id = ?", 
                (nome, autor_id)
            )
            mensagem = "Autor atualizado com sucesso!"
        else:
            cursor.execute(
                "INSERT INTO autor (nome_autor) VALUES (?)", 
                (nome,)
            )
            mensagem = "Autor cadastrado com sucesso!"
            
        conn.commit()
        conn.close()
        messagebox.showinfo("Sucesso", mensagem)
        janela_cad.destroy()

    btn_texto = "Atualizar" if autor_id else "Cadastrar"
    btn_cor = "#ffcc00" if autor_id else "lightgreen"
    
    tk.Button(janela_cad, text=btn_texto, command=salvar, bg=btn_cor).pack(pady=20)


def abrir_consulta_autor(parent):
    janela_con = tk.Toplevel(parent)
    janela_con.title("Consultar Autores")
    janela_con.geometry("500x480") 

    colunas = ("ID", "Nome do Autor")
    tabela = ttk.Treeview(janela_con, columns=colunas, show="headings")
    tabela.heading("ID", text="ID")
    tabela.heading("Nome do Autor", text="Nome do Autor")
    tabela.column("ID", width=50, anchor="center")
    tabela.pack(pady=20, padx=10, fill="both", expand=True)

    def executar_edicao():
        item = tabela.selection()

        if not item:
            messagebox.showwarning("Aviso", "Selecione um autor!")
            return

        valores = tabela.item(item, "values")
        aut_id = int(valores[0])

        abrir_cadastro_autor(parent, autor_id=aut_id)
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
    cursor.execute("SELECT * FROM autor")
    
    for linha in cursor.fetchall():
        tabela.insert("", tk.END, values=linha)
    
    conn.close()