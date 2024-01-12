import textwrap

'''
Criamos as funções de acordo com o desafio final

'''

def menu():
    menu = """\n
    -----------MENU----------
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo Usuario
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))

def depositar(saldo,valor,extrato,/):
    if valor > 0:
        saldo += valor
        extrato += f"Deposito:\tR$:{valor:.2f}\n"
        print("\n @@@ Depósito realizado com sucesso! @@@")
    else:
        print("\n### Operação falhou o valor informado é invalido. ###")
        
    return saldo, extrato

def sacar(*,saldo,valor,extrato,limite,numero_saques,limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques > limite_saques

    if excedeu_saldo:
        print("\n ### Operação falhou! Saldo insuficiente. ###")

    elif excedeu_limite:
        print("\n ### Operação falhou! O valor do saque excede limite. ###")

    elif excedeu_saques:
        print("\n### Operação falhou! Numero maximo de saques excedido ###")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: \t\tR$:{valor:.2f}\n"
        numero_saques += 1
        print("\n @@@ Saque realizado com sucesso! @@@")

    else:
        print("\n@@@ Operação falhou! O valor informado é invalido. @@@")

    return saldo,extrato

def exibir_extrato(saldo,/,*, extrato):
    print("\n============Extrato==========")
    print("Não foram realizadas movimentações."if not extrato else extrato)
    print(f"\nSaldo: \t\tR$:{saldo:.2f}")
    print("===============================")
    return

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n ### Já existe usuario com esse CPF! ###")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento(dd-mm-aaaa):")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado):")

    usuarios.append({"nome":nome,"data_nascimento":data_nascimento,"cpf":cpf,"endereco":endereco})

    print("@@@ Usuario cadastrado com sucessso!@@@")

def filtrar_usuario(cpf,usuario):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf" == cpf]
                          return usuarios_filtrados[0] if usuarios_filtrados else None
    return

def criar_conta(agencia, numero_conta, usuario):
    return
def lista_contas(contas):
    return

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    conta = []

    while True:
        opcao = menu()

        if opcao =="d":
            valor = float(input("Informe o valor de deposito: "))

            saldo, extrato = depositar(saldo,valor,extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES
                )

        elif opcao =="e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_contas(AGENCIA, numero_conta,usuarios)
        
            if conta:
                contas.append(conta)

        elif opcao =="lc":
            lista_contas(contas)

        elif opcao == "q":
            break
            
        else:
            print("Operação invalida, por favor selecione novamente a operação desejada.")

            

main()
