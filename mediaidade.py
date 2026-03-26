17soma = 0
cont = 0

idade = int(input("Sua idade: "))

while idade != 0:
        
    cont += 1
    soma += idade
    idade = int(input("Sua idade: "))
        
    if cont > 0:
        mediaIdade = soma/cont
print(f"A média da idade é {mediaIdade:.1f}")
        