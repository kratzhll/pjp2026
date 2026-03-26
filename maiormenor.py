for i in range(1,16):
    
    num = int(input("O seu número: "))
    
    if i == 1:
        maior = num 
        menor = num
        
    else: 
        if num > maior:
            maior = num
           
        if num < menor:
            menor = num
        
print(f"O número maior é {maior}\n")
print(f"O número menor é {menor}")