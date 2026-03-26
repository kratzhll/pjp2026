anterior = 0
atual = 1

print(f"Sequência de Fibonacci: \n{anterior} \n{atual}")

for i in range(3,11):
    
    proximo = anterior + atual
    
    anterior = atual
    
    atual = proximo
    
    print(f"{proximo}")
        