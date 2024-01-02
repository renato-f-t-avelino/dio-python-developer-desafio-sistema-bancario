# Main file

menu = """
     Escolha uma opção

  [d] Depositar
  [s] Sacar
  [e] Exibir Extrato
  [q] Sair


=> """


LIMITE_SAQUE=500
LIMITE_NUM_SAQUES=3
operacoes = []
saldo = 0
saque_numero = 0


while (True):

    opcao = input(menu)

    if (opcao == "d"):
        print("Entre com o valor a ser depositado: ", end="")
        valor = float(input())
        if ((valor <= 0)):
            print("Valor inválido")
        else:
            operacoes.append(f"Depósito de R$ {valor:.2f}")
            saldo += valor
            print("Depósito realizado com sucesso")
    
    elif (opcao == "s"):
        print("Entre com o valor a ser sacado: ", end="")
        valor = float(input())
        if (saque_numero >= LIMITE_NUM_SAQUES):
            print("Número máximo de saques atingido")
        elif (valor > saldo):
            print("Saldo insuficiente para o saque")
        elif (valor > LIMITE_SAQUE):
            print(f"Não foi possível realizar o saque. O valor máximo por operação de saque é de {LIMITE_SAQUE}")
        else:
            operacoes.append(f"Saque de R$ {valor:.2f}")
            saldo -= valor
            saque_numero += 1
            print("Saque realizado com sucesso")

    elif (opcao == "e"):
        if not operacoes:
            print("Nenhuma operação executada ainda")
        else:
            print("----- Extrato -----")
            for item in operacoes:
                print(item)
            print("-------------------")
        print(f"Saldo atual: R$ {saldo:.2f}")
            
    elif (opcao == "q"):
        print("Fim da operação")
        break

    else:
        print("Opção inválida")


