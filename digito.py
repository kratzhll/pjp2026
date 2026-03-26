soma = 0

numero = int(input("Digite o seu número para realizar uma soma dos dígitos: "))

while numero > 0:
        
    
    digito = numero % 10
    
    soma = soma + digito
    
    numero = numero // 10
        
print(f"A soma do dígito informado resulta em {soma}")
        