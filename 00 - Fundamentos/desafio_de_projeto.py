menu = """
====== MENU ======
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [0] Sair
==================
Opção: """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        print("====== Operação de Depósito ======")
        valor = int(input("Informe o valor que deseja depositar: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Valor depositado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "2":
        print("====== Operação de Saque ======")
        valor = float(input("Informe o valor que deseja sacar: "))
        limite_maximo_saque = 500

        if numero_saques == LIMITE_SAQUES or valor > limite_maximo_saque:
            print("Não será possível sacar o valor informado, limite de saque diário atingido ou valor acima do limite de saque!")

        elif saldo >= valor and valor <= limite_maximo_saque:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("Operação realizada com sucesso, pode retirar seu dinheiro na boca do caixa!")
        else:
            print("Não será possível sacar o valor informado por falta de saldo!")

      

    elif opcao == "3":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "0":
        print("""
    Obrigado por nos escolher como seu banco!
              
    Sistema Encerrado!""")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")