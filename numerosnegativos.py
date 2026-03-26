cont = 0

for i in range(1,11):
    
    numero = int(input("Número: "))
        
    if numero < 0:
        cont += 1
        
print(f"Os números negativos apareceram {cont} vez(es)")
        