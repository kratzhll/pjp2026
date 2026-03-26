def saudar_cliente():
    print("Bem-vindo à TechCoffee!")
    print("O que deseja pedir hoje?")

saudar_cliente()

def saudar_personalizado(nome):
    print(f"Olá {nome}! Seu café favorito já está sendo preparado.")

# Chamando a função:
saudar_personalizado("Seu Arnaldo")
saudar_personalizado("Fernando")

def soma (n1,n2):
    resultado = n1 + n2
    print("O resultado é", resultado)

# Chamando a função
soma (18,20)

def subtracao (n1,n2):
    resultado = n1 - n2
    print("O resultado é", resultado)

# Chamando a função
subtracao (18,20)

def divisao (n1,n2):
    resultado = n1 / n2
    print("O resultado é", resultado)

# Chamando a função
divisao (18,18)

def multi (n1,n2):
    resultado = n1 * n2
    print("O resultado é", resultado)

# Chamando a função
multi (2,2)

def calcular_total(quantidade, preço_unitario):
    total = quantidade * preço_unitario
    return total

#Guardando o resultado em uma variável
valor_da_venda = calcular_total(3, 5,50)
print(f"O valor a pagar é: R${valor_da_venda}")
