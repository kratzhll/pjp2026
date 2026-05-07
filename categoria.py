import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# --- BANCO DE DADOS ---
def conectar():
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS categorias (
            categorias_id INTEGER PRIMARY KEY AUTOINCREMENT, 
            categorias_nome VARCHAR(100) NOT NULL
        )
    """)
    conn.commit()
    return conn

# --- LÓGICA DAS TELAS ---

def abrir_cadastro(parent, categorias_id=None):
    janela_cad = tk.Toplevel(parent)
    janela_cad.title("Editar Categoria" if categorias_id else "Cadastrar Categoria")
    janela_cad.geometry("350x200")
    
    tk.Label(janela_cad, text="Nome da Categoria:", font=("Arial", 10)).pack(pady=10)
    ent_nome = tk.Entry(janela_cad, width=30)
    ent_nome.pack(pady=5)

    # Se for EDIÇÃO, preenche o campo com o nome atual
    if categorias_id:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT categorias_nome FROM categorias WHERE categorias_id = ?", (categorias_id,))
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
        
        if categorias_id:
            # Lógica de Atualização
            cursor.execute("UPDATE categorias SET categorias_nome = ? WHERE categorias_id = ?", (nome, categorias_id))
            mensagem = "Categoria atualizada com sucesso!"
        else:
            # Lógica de Inserção
            cursor.execute("INSERT INTO categorias (categorias_nome) VALUES (?)", (nome,))
            mensagem = "Categoria cadastrada com sucesso!"
            
        conn.commit()
        conn.close()
        messagebox.showinfo("Sucesso", mensagem)
        janela_cad.destroy()

    btn_texto = "Atualizar" if categorias_id else "Cadastrar"
    btn_cor = "#ffcc00" if categorias_id else "lightgreen"
    
    tk.Button(janela_cad, text=btn_texto, command=salvar, bg=btn_cor).pack(pady=20)

def abrir_consulta(parent):
    janela_con = tk.Toplevel(parent)
    janela_con.title("Consultar Categorias")
    janela_con.geometry("500x480") 

    # 1. Tabela (Treeview)
    colunas = ("ID", "Nome da Categoria")
    tabela = ttk.Treeview(janela_con, columns=colunas, show="headings")
    tabela.heading("ID", text="ID")
    tabela.heading("Nome da Categoria", text="Nome da Categoria")
    tabela.column("ID", width=50, anchor="center")
    tabela.pack(pady=20, padx=10, fill="both", expand=True)

    # 2. Função interna para o botão Editar
    def executar_edicao():
        item_selecionado = tabela.selection()
        
        if not item_selecionado:
            messagebox.showwarning("Aviso", "Por favor, selecione uma categoria na lista!")
            return

        valores = tabela.item(item_selecionado, "values")
        cat_id = int(valores[0])

        # Abre a mesma tela de cadastro, mas agora enviando o ID para modo edição
        abrir_cadastro(parent, categorias_id=cat_id)
        janela_con.destroy() 

    # 3. Botões de Ação
    frame_botoes = tk.Frame(janela_con)
    frame_botoes.pack(pady=10)

    btn_editar = tk.Button(
        frame_botoes, 
        text="Editar Selecionada", 
        command=executar_edicao,
        bg="#ffcc00",
        font=("Arial", 10, "bold"),
        width=20
    )
    btn_editar.pack(side="left", padx=5)

    # 4. Buscar dados iniciais
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM categorias")
    for linha in cursor.fetchall():
        tabela.insert("", tk.END, values=linha)
    conn.close()