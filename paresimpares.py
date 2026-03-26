par = 0
impar = 0

for i in range(1,11):
    
    num = int(input("O seu número: "))
    
    if num % 2 == 0:
        par += num 
    else:
        impar += num
        
print(f"A soma dos pares é {par} \n")
print(f"A soma dos ímpares é {impar}")