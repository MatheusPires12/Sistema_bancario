import textwrap

def menu():
    menu = """\n
    =============MENU==============

    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tNova conta
    [5]\tListar contas
    [6]\tNovo usuário
    [0]\tSair
    =>    """
    
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Deposito:\tR$ {valor:.2f}\n"
        print(f"\nDeposito de R$ {valor:.2f}, realizado com sucesso!")

    else:
        print("\nOperação falhou! O valor informado é inválido.")
    
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Você não tem saldo suficiente, tente novamente com outro valor.") 

    elif excedeu_limite:
        print("O limite do saque é de R$ 500, tente novamente com outro valor.")

    elif excedeu_saques:
        print("Limite de saques diários atingido, tente novamente amanhã.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f}, realizado com sucesso!")  

    else:
        print("Operação falhou! O valor informado é inválido!")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    if extrato == "":
        print("\n============EXTRATO============\n")
        print("Não foram realizadas movimentações.")
        print("\n================================")

    else:
        print("\n============EXTRATO============\n")
        print(extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n===============================")

def criar_usuario(usuarios):
    cpf = input("Informe o seu CPF (somente números): ")

    if cpf.isnumeric() == True and len(cpf) == 11:
        usuario = filtrar_usuario(cpf, usuarios)

        if usuario:
            print("Já existe um usuário com esse CPF!")
            return
        
        nome = input("Informe o nome completo: ")
        data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
        endereco = input("Informe o endereço (logradouro, número - bairro - cidade/sigla estado): ")
        usuarios.append({"nome":nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
        print("Usuário criado com sucesso!")

    else:
        print("CPF inválido! Tente novamente!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta_corrente(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("Usuário não encontrado, fluxo de criação de conta encerrado!")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print('='*32)
        print(textwrap.dedent(linha))

def main():
    LIMITE_DE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    numero_conta = 1

    while(True):

        opcao = menu()

        if opcao == "1":
            valor = float(input("Informe o valor que deseja depositar:\nR$ "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "2":
            valor = float(input("Informe o valor que deseja sacar:\nR$ "))
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_DE_SAQUES,
            )

        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "4":
            conta = criar_conta_corrente(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
                numero_conta += 1 
        
        elif opcao == "5":
            if len(contas) == 0:
                print("Nenhuma conta foi criada!")
                
            else:
                listar_contas(contas)

        elif opcao == "6":
            criar_usuario(usuarios)

        elif opcao == "0":
            break

        else:
            print("Opção inválida, tente novamente!")

main()

