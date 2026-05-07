import tkinter as tk

def montar_tela_login(container, comando_entrar):
    # Limpa a janela caso haja algo nela
    for widget in container.winfo_children():
        widget.destroy()

    tk.Label(container, text="Login de Acesso", font=("Arial", 12, "bold")).pack(pady=10)

    tk.Label(container, text="Usuário:").pack()
    ent_usuario = tk.Entry(container)
    ent_usuario.pack(pady=5)

     # Botão que executa a função de validação que virá do main.py
    btn = tk.Button(container, text="Entrar", command=lambda: comando_entrar(ent_usuario.get()))
    btn.pack(pady=20)
 