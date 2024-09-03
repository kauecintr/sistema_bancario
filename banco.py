menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 0
extrato = ""
numero_saques = 0
LIMITE_saques = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Quanto deseja depositar? "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Valor inválido")



    elif opcao == "s":
            valor = float(input("Quanto deseja sacar? "))
            excedeu_saldo = valor > saldo
            excedeu_limite = valor > limite
            excedeu_saques = numero_saques >= LIMITE_saques

            if excedeu_saldo:
                print("Voce não tem suficiente")

            elif excedeu_limite:
                print("Limite excedido")

            elif excedeu_saques:
                print("Limite de saques excedido")

            elif valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1

            else:
                print("Valor inválido")




    elif opcao == "e":
            print("\n###########Extrato############")
            print("Não há extrato." if not extrato else extrato)
            print(f"Saldo: R$ {saldo:.2f}")
            print("##############################\n")



    elif opcao == "q":
            break
    
    else:
        print("Opção inválida")