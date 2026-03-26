primo = True

n = int(input("Informe o seu número para verificar o primo: "))

if n <= 1:
    primo = False
else:
    for i in range(2,n):
        if n % i == 0:
            primo = False
            break
            
if primo:
        
    print(f"O número {n} é um número primo")
        
else:
        
    print(f"O número {n} não é um número primo")
        