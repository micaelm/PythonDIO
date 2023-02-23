menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:

    opcao = input(menu)

    if opcao =="d":
        print("Deposito")
        dep = int(input("Qual quantidade que deseja depositar: "))
        if saldo < 0:
            print(" Operação inválida, não é possivel deposito negativo!")
        else:
            saldo+=dep
            print(f"Foi depositado em sua conta o valor de R$:{saldo:.2f}")
    elif opcao =="s":
        print("Saque")
        saque = int(input("Qual valor deseja sacar: "))   
        if LIMITE_SAQUES < 1:
            print("Limite de saque atigindo!!")
        else:
            if saque <= 500 and saque <= saldo:
                LIMITE_SAQUES-=1
                saldo-=saque
                extrato+=f"Saque de {saque:.2f}\n"
                print(f"Saque de R$:{saque} efetuado com sucesso!!")
            elif saque >= 600 :
                print("Saque maior que o permitido!!")
            elif saque > saldo:
                print("Sua conta está sem saldo!!")
            else:
                print("Não será possivel sacar o dinheiro por falta de saldo")

    elif opcao =="e":
        if not extrato:
            print("---------------------------------Extrato---------------------------------")
            print("Não foram realizadas movimentações")
        else:
            print("---------------------------------Extrato---------------------------------")
            print(f"{extrato}")
            print(f"Saldo em conta de R$:{saldo:.2f}")

    elif opcao =="q":
        print("Saindo do sistema")
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

