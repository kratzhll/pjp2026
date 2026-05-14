import tkinter as tk
from tkinter import messagebox
import banco_dados as bd

def montar_tela_emprestimo(container, funcao_voltar):

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
        text="Gerenciar Empréstimos",
        font=("Arial", 14, "bold")
    ).pack(pady=10)

    # --- FORMULÁRIO ---

    # LIVRO ID
    tk.Label(
        container,
        text="ID do Livro:",
        font=("Arial", 10, "bold")
    ).pack(pady=5)

    ent_livro = tk.Entry(container, width=40)
    ent_livro.pack()

    # CLIENTE ID
    tk.Label(
        container,
        text="ID do Cliente:",
        font=("Arial", 10, "bold")
    ).pack(pady=5)

    ent_cliente = tk.Entry(container, width=40)
    ent_cliente.pack()

    # STATUS
    tk.Label(
        container,
        text="Status do Livro:",
        font=("Arial", 10, "bold")
    ).pack(pady=5)

    ent_status = tk.Entry(container, width=40)
    ent_status.pack()

    # DATA EMPRESTIMO
    tk.Label(
        container,
        text="Data do Empréstimo:",
        font=("Arial", 10, "bold")
    ).pack(pady=5)

    ent_data_ped = tk.Entry(container, width=40)
    ent_data_ped.pack()

    # DATA DEVOLUÇÃO
    tk.Label(
        container,
        text="Data de Devolução:",
        font=("Arial", 10, "bold")
    ).pack(pady=5)

    ent_data_dev = tk.Entry(container, width=40)
    ent_data_dev.pack()

    # SALVAR
    def salvar():

        livro_id = ent_livro.get()
        cliente_id = ent_cliente.get()
        status_livro = ent_status.get()
        data_ped = ent_data_ped.get()
        data_dev = ent_data_dev.get()

        if livro_id and cliente_id and status_livro and data_ped and data_dev:

            bd.db_cadastrar_emprestimos(
                livro_id,
                cliente_id,
                status_livro,
                data_ped,
                data_dev
            )

            messagebox.showinfo(
                "Sucesso",
                "Empréstimo cadastrado com sucesso!"
            )

            ent_livro.delete(0, tk.END)
            ent_cliente.delete(0, tk.END)
            ent_status.delete(0, tk.END)
            ent_data_ped.delete(0, tk.END)
            ent_data_dev.delete(0, tk.END)

            atualizar_lista()

        else:
            messagebox.showwarning(
                "Aviso",
                "Preencha todos os campos!"
            )

    tk.Button(
        container,
        text="Cadastrar Empréstimo",
        command=salvar,
        bg="green",
        fg="white"
    ).pack(pady=10)

    # --- LISTA ---
    tk.Label(
        container,
        text="Empréstimos Cadastrados:",
        font=("Arial", 10, "bold")
    ).pack(pady=10)

    lista_frame = tk.Frame(container)
    lista_frame.pack(fill="both", expand=True, padx=20)

    def atualizar_lista():

        for widget in lista_frame.winfo_children():
            widget.destroy()

        emprestimos = bd.db_listar_emprestimos()

        for c in emprestimos:

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
                f"Livro: {c[1]} | "
                f"Cliente: {c[2]} | "
                f"Status: {c[3]}"
            )

            tk.Label(
                lista_frame,
                text=texto
            ).grid(row=c[0], column=1, sticky="w")

    def deletar(id_c):

        if messagebox.askyesno(
            "Confirmar",
            "Deseja excluir este empréstimo?"
        ):

            bd.db_deletar_emprestimos(id_c)

            atualizar_lista()

    atualizar_lista()