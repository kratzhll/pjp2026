def verificar_caldeira (temp_atual):
    if temp_atual < 90:
        return print("Aquecendo")
    elif temp_atual <= 100:
        return print("Pronta para uso.")
    if temp_atual > 100:
        return print("PERIGO: Superaquecimento!")

    
verificar_caldeira(200)