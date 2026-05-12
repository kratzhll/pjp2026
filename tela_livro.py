import tkinter as tk
from tkinter import messagebox
import banco_dados as bd

def montar_tela_livro(container, funcao_voltar):
    for widget in container.winfo_children():
        widget.destroy()

# --- BOTÃO VOLTAR ---
    # Ele fica no topo para fácil acesso
    tk.Button(container, text="← Voltar ao Menu", command=funcao_voltar, bg="#ccc").pack(anchor="nw", padx=10, pady=5)

    # --- Título da Tela ---
    tk.Label(container, text="Cadastro de Livros", font=("Arial", 14, "bold")).pack(pady=10)
    # --- Formulário de Cadastro ---
    tk.Label(container, text="Título do Livro:", font=("Arial", 10, "bold")).pack(pady=5)
    ent_titulo = tk.Entry(container, width=40)
    ent_titulo.pack()

    tk.Label(container, text="Autor:", font=("Arial", 10, "bold")).pack(pady=5)
    ent_autor = tk.Entry(container, width=40)
    ent_autor.pack()

    def salvar():
        titulo = ent_titulo.get()
        autor = ent_autor.get()
        if titulo and autor:
            bd.db_cadastrar_livro(titulo, autor)
            messagebox.showinfo("Sucesso", "Livro cadastrado com sucesso!")
            ent_titulo.delete(0, tk.END)
            ent_autor.delete(0, tk.END)
            atualizar_lista()
        else:
            messagebox.showwarning("Aviso", "Preencha todos os campos!")

    tk.Button(container, text="Cadastrar Livro", command=salvar, bg="green", fg="white").pack(pady=10)

    # --- Lista de Livros ---
    tk.Label(container, text="Livros Cadastrados:", font=("Arial", 10, "bold")).pack(pady=10)
    
    lista_frame = tk.Frame(container)
    lista_frame.pack(fill="both", expand=True, padx=20)

    def atualizar_lista():
        # Limpa a lista atual para recarregar
        for widget in lista_frame.winfo_children():
            widget.destroy()
        
        livros = bd.db_listar_livros()
        for l in livros:
            btn_del = tk.Button(lista_frame, text="X", fg="white", bg="red", 
                               command=lambda id_l=l[0]: deletar(id_l))
            btn_del.grid(row=l[0], column=0, padx=5, pady=2)
            
            texto = f"ID: {l[0]} | Livro: {l[1]} | Autor: {l[5]} [{l[4]}]"
            tk.Label(lista_frame, text=texto).grid(row=l[0], column=1, sticky="w")

    def deletar(id_l):
        if messagebox.askyesno("Confirmar", "Deseja excluir este livro?"):
            bd.db_deletar_livro(id_l)
            atualizar_lista()

    atualizar_lista()