import tkinter as tk
from tela_login import montar_tela_login
from tela_principal import montar_tela_principal

def validar_e_entrar(usuario):
# Lógica de validação simples

    if usuario == "admin":
        montar_tela_principal(root) 
    else:
        print("Usuário incorreto!")

root = tk.Tk()
root.title("Tela Login")
root.geometry("300x250")

montar_tela_login(root, validar_e_entrar)

root.mainloop()