import tkinter as tk
from tkinter import ttk, messagebox
import categoria
import livros
import autor
import editora

def abrir_principal():

    # --- MENU PRINCIPAL (ROOT) ---
    root = tk.Tk()
    root.protocol("WM_DELETE_WINDOW", root.quit)
    root.title("Menu Principal - Sistema de Biblioteca")
    root.geometry("400x500")

    # 1. Criar a barra de menu principal
    barra_menu = tk.Menu(root)

    # 2. Criar o menu "Categorias"
    menu_categorias = tk.Menu(barra_menu, tearoff=0)
    menu_categorias.add_command(label="Cadastrar Nova", command=lambda: categoria.abrir_cadastro(root))
    menu_categorias.add_command(label="Consultar Todas", command=lambda: categoria.abrir_consulta(root))
    menu_categorias.add_separator()
    menu_categorias.add_command(label="Sair", command=root.quit)

    # 3. Criar o menu "Livros"
    menu_livros = tk.Menu(barra_menu, tearoff=0)
    menu_livros.add_command(label="Cadastrar Novo", command=lambda: livros.abrir_cadastro_livro(root))
    menu_livros.add_command(label="Consultar Todos", command=lambda: livros.abrir_consulta_livros(root))
    menu_livros.add_separator()
    menu_livros.add_command(label="Sair", command=root.quit)

    #44 Editoras
    menu_editora = tk.Menu(barra_menu, tearoff=0)
    menu_editora.add_command(label="Cadastrar Novo", command=lambda: editora.abrir_cadastro(root))
    menu_editora.add_command(label="Consultar Todos", command=lambda: editora.abrir_consulta(root))
    menu_editora.add_separator()
    menu_editora.add_command(label="Sair", command=root.quit)

    # 4. Adicionar menus à barra principal
    barra_menu.add_cascade(label="Categorias", menu=menu_categorias)
    barra_menu.add_cascade(label="Livros", menu=menu_livros)
    barra_menu.add_cascade(label="Editoras", menu=menu_editora)

    # 5. Configurar a janela para usar esta barra de menu
    root.config(menu=barra_menu)

    tk.Label(root, text="GERENCIADOR BIBLIOTECA", font=("Arial", 14, "bold")).pack(pady=30)

    btn_cadastrar = tk.Button(
        root, text="NOVO CADASTRO CATEGORIA", width=25, height=2,
        command=lambda: categoria.abrir_cadastro(root), bg="#e1e1e1"
    )
    btn_cadastrar.pack(pady=10)

    btn_consultar = tk.Button(
        root,
        text="LISTA DE CATEGORIAS",
        command=lambda: categoria.abrir_consulta(root),
        bg="#e1e1e1"
    )
    btn_consultar.pack(pady=10)

    btn_cadastrar_livro = tk.Button(
        root, text="NOVO CADASTRO LIVRO", width=25, height=2,
        command=lambda: livros.abrir_cadastro_livro(root), bg="#e1e1e1"
    )
    btn_cadastrar_livro.pack(pady=10)

    btn_consultar_livro = tk.Button(
        root,
        text="LISTA DE LIVROS",
        command=lambda: livros.abrir_consulta_livros(root),
        bg="#e1e1e1"
    )
    btn_consultar_livro.pack(pady=10)

    btn_cadastrar_autor = tk.Button(
        root, text="NOVO CADASTRO AUTOR", width=25, height=2,
        command=lambda: autor.abrir_cadastro_autor(root), bg="#e1e1e1"
    )
    btn_cadastrar_autor.pack(pady=10)

    btn_consultar_autor = tk.Button(
        root,
        text="LISTA DE AUTORES",
        command=lambda: autor.abrir_consulta_autor(root),
        bg="#e1e1e1"
    )
    btn_consultar_autor.pack(pady=10)

    btn_sair = tk.Button(root, text="SAIR", width=25, command=root.quit, fg="red")
    btn_sair.pack(pady=20)

    root.mainloop()