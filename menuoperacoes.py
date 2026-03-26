while True:
    opcao = int(input("1) Somar, 2) Subtrair, 3) Sair, escolha uma opção: "))

    match opcao:
        case 1:
            n1 = int(input("Primeiro Número: "))
            n2 = int(input("Segundo Número: "))

            res = n1 + n2
            print(f"A soma entre {n1} e {n2} resulta em {res}\n")

        case 2:
            n1 = int(input("Primeiro Número: "))
            n2 = int(input("Segundo Número: "))

            res = n1 - n2
            print(f"A subtração entre {n1} e {n2} resulta em {res}\n")

        case 3:
            print("Encerrado")
            break

        case _:
            print("A escolha da sua opção é inválida\n")