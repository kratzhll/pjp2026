import tkinter as tk
from tela_livro import montar_tela_livro

def montar_menu_principal():
    # Limpa a tela para voltar ao menu
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Bem-vindo ao Sistema", font=("Arial", 16)).pack(pady=20)
    
    # Passamos a função 'montar_menu_principal' para a tela de livro
    tk.Button(root, text="Abrir Cadastro de Livros", 
              command=lambda: montar_tela_livro(root, montar_menu_principal), 
              width=30, height=2).pack(pady=10)

root = tk.Tk()
root.title("Sistema de Biblioteca Escolar")
root.geometry("500x600")

# Inicia o sistema desenhando o menu
montar_menu_principal()

root.mainloop()