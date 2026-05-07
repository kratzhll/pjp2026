import tkinter as tk
import principal

def montar_tela_principal(container):
    # Limpa a tela de login para desenhar a principal
    for widget in container.winfo_children():
        widget.destroy()

    container.title("Sistema Interno")
    tk.Label(container, text="Área Restrita", fg="green", font=("Arial", 14)).pack(pady=20)
    tk.Label(container, text="Bem-vindo ao sistema principal!").pack()
    
    tk.Button(container, text="Abrir Biblioteca", command=lambda: abrir_biblioteca(container)).pack(pady=20)

def abrir_biblioteca(container):

    container.destroy()

    principal.abrir_principal()