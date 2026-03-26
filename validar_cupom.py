def validar_cupom (codigo):
    if codigo == "CAFÉ10":
        return 0.10
    elif codigo == "PROMO5":
        return 0.05
    else:
        return 0 
    
    #chamando

print(validar_cupom("CAFÉ10"))
print(validar_cupom("PROMO5"))
print(validar_cupom("abc"))