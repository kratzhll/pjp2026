def converter_real_para_dolar(valor_real, cotacao_dolar):
    return valor_real / cotacao_dolar

#Pedindo os valores em reais com input e pedindo a cotação

valor_real = int(input("Digite o valor em reais: "))
cotacao = 5

valor_em_dolar = converter_real_para_dolar(valor_real, cotacao)

print(f"R${valor_real} = US${valor_em_dolar:}")