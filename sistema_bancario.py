menu = """
======MENU======

[d] = Depositar
[s] = Sacar
[e] = Extrato
[q] = Sair

================
"""

saldo = 0
limite = 500
extrato = ""
numero_de_saques = 0
LIMITE_DE_SAQUES = 3

def depositar(deposito):
    global saldo, extrato
    if deposito > 0:
        saldo += deposito
        print(f"Deposito de R$ {deposito:.2f}, realizado com sucesso!")
        extrato += f"Deposito: R$ {deposito:.2f}\n"
    else:
        print("Valor inválido, tente novamente!")

def sacar(saque):
    global saldo, extrato, numero_de_saques

    if numero_de_saques == LIMITE_DE_SAQUES:
        print("Limite de saques diários atingido, tente novamente amanhã.")
    elif saque > limite:
        print("O limite do saque é de R$ 500, tente novamente com outro valor.")
    else:
        if saque > saldo or saque < 0:
            print("Não foi possivel realizar o saque, tente outro valor.")
        else:
            saldo -= saque
            print(f"Saque de R$ {saque:.2f}, realizado com sucesso!")
            extrato += f"Saque: R$ {saque:.2f}\n"
            numero_de_saques += 1

while(True):

    opcao = input(menu)

    if opcao == "d":
        deposito = float(input("Informe o valor que deseja depositar:\nR$ "))
        depositar(deposito)
    elif opcao == "s":
        saque = float(input("Informe o valor que deseja sacar:\nR$ "))
        sacar(saque)
    elif opcao == "e":
        if extrato == "":
            print("\n============EXTRATO============\n")
            print("Não foram realizadas movimentações.")
            print("\n================================")
        else:
            print("\n============EXTRATO============\n")
            print(extrato)
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("\n===============================")
    elif opcao == "q":
        break
    else:
        print("Opção inválida, tente novamente!")
