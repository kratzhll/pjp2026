import tkinter as tk
from tkinter import messagebox
import banco_dados as bd

def montar_tela_clientes(container, funcao_voltar):

    for widget in container.winfo_children():
        widget.destroy()

    # --- BOTÃO VOLTAR ---
    tk.Button(
        container,
        text="← Voltar ao Menu",
        command=funcao_voltar,
        bg="#ccc"
    ).pack(anchor="nw", padx=10, pady=5)

    # --- TÍTULO ---
    tk.Label(
        container,
        text="Gerenciar Clientes",
        font=("Arial", 14, "bold")
    ).pack(pady=10)

    # --- FORMULÁRIO ---

    # NOME
    tk.Label(
        container,
        text="Nome do Cliente:",
        font=("Arial", 10, "bold")
    ).pack(pady=5)

    ent_nome = tk.Entry(container, width=40)
    ent_nome.pack()

    # CIDADE
    tk.Label(
        container,
        text="Cidade:",
        font=("Arial", 10, "bold")
    ).pack(pady=5)

    ent_cidade = tk.Entry(container, width=40)
    ent_cidade.pack()

    # EMAIL
    tk.Label(
        container,
        text="Email:",
        font=("Arial", 10, "bold")
    ).pack(pady=5)

    ent_email = tk.Entry(container, width=40)
    ent_email.pack()

    # SALVAR
    def salvar():

        nome_cliente = ent_nome.get()
        cidade = ent_cidade.get()
        email = ent_email.get()

        if nome_cliente and cidade and email:

            bd.db_cadastrar_cliente(
                nome_cliente,
                cidade,
                email
            )

            messagebox.showinfo(
                "Sucesso",
                "Cliente cadastrado com sucesso!"
            )

            ent_nome.delete(0, tk.END)
            ent_cidade.delete(0, tk.END)
            ent_email.delete(0, tk.END)

            atualizar_lista()

        else:
            messagebox.showwarning(
                "Aviso",
                "Preencha todos os campos!"
            )

    tk.Button(
        container,
        text="Cadastrar Cliente",
        command=salvar,
        bg="green",
        fg="white"
    ).pack(pady=10)

    # --- LISTA ---
    tk.Label(
        container,
        text="Clientes Cadastrados:",
        font=("Arial", 10, "bold")
    ).pack(pady=10)

    lista_frame = tk.Frame(container)
    lista_frame.pack(fill="both", expand=True, padx=20)

    def atualizar_lista():

        for widget in lista_frame.winfo_children():
            widget.destroy()

        clientes = bd.db_listar_clientes()

        for c in clientes:

            btn_del = tk.Button(
                lista_frame,
                text="X",
                fg="white",
                bg="red",
                command=lambda id_c=c[0]: deletar(id_c)
            )

            btn_del.grid(row=c[0], column=0, padx=5, pady=2)

            texto = (
                f"ID: {c[0]} | "
                f"Nome: {c[1]} | "
                f"Cidade: {c[2]} | "
                f"Email: {c[3]}"
            )

            tk.Label(
                lista_frame,
                text=texto
            ).grid(row=c[0], column=1, sticky="w")

    def deletar(id_c):

        if messagebox.askyesno(
            "Confirmar",
            "Deseja excluir este cliente?"
        ):

            bd.db_deletar_cliente(id_c)

            atualizar_lista()

    atualizar_lista()