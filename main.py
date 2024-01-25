# Main file

menu = """
     Escolha uma opção

  [d] Depositar
  [s] Sacar
  [e] Exibir Extrato
  [nu] Novo Usuário
  [nc] Nova Conta
  [lu] Lista Usuários
  [lc] Lista Contas
  [q] Sair


=> """

NUM_AGENCIA = "0001"
LIMITE_SAQUE=500
LIMITE_NUM_SAQUES=3

operacoes = []
saldo = 0
saque_numero = 0
num_contas_total = 0

usuarios = []
contas = []

#---------------------------------------------------------------------------------------------------------
# Função saque
def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if (numero_saques >= limite_saques):
        print("Número máximo de saques atingido")
    elif (valor > saldo):
        print("Saldo insuficiente para o saque")
    elif (valor > limite):
        print(f"Não foi possível realizar o saque. O valor máximo por operação de saque é de {limite}")
    else:
        extrato.append(f"Saque de R$ {valor:.2f}")
        saldo -= valor
        numero_saques += 1
        print("Saque realizado com sucesso")
    return saldo, numero_saques

#---------------------------------------------------------------------------------------------------------
# Função deposito
def deposito(saldo, valor, extrato, /):
    if ((valor <= 0)):
        print("Valor inválido")
    else:
        extrato.append(f"Depósito de R$ {valor:.2f}")
        saldo += valor
        print("Depósito realizado com sucesso")
    return saldo

#---------------------------------------------------------------------------------------------------------
# Função extrato
def extrato_conta(saldo, /, *, extrato):
    if not extrato:
        print("Nenhuma operação executada ainda")
    else:
        print("----- Extrato -----")
        for item in extrato:
            print(item)
        print("-------------------")
    print(f"Saldo atual: R$ {saldo:.2f}")

#---------------------------------------------------------------------------------------------------------
# Função busca_usuario_cpf
def busca_usuario_cpf(*, lista_usuarios, cpf):
    for indice, usuario in enumerate(lista_usuarios):
        if (usuario.get("cpf") == cpf):
            return indice
    return -1

#---------------------------------------------------------------------------------------------------------
# Função criar_usuario
def criar_usuario(*, lista_usuarios, nome, nascimento, cpf, ender_logradouro, ender_num, ender_bairro, ender_cidade, ender_estado):
    if busca_usuario_cpf(lista_usuarios=lista_usuarios, cpf=cpf) >= 0:
        print("CPF já utilizado. Conta não pode ser criada.")
        return
    novo_usuario = dict(nome=nome, nascimento=nascimento, cpf=cpf, endereco=ender_logradouro + ", " + ender_num + " - " + ender_bairro + " - " + ender_cidade + "/" + ender_estado)
    lista_usuarios.append(novo_usuario)
    print("Usuário criado com sucesso")

#---------------------------------------------------------------------------------------------------------
# Função criar_conta
def criar_conta(*, lista_contas, agencia, num_conta, cpf_usuario):
    if busca_usuario_cpf(lista_usuarios=usuarios, cpf=f'{cpf}') < 0:
        print("Não foi encontrado usuário com o CPF informado")
        return num_conta

    num_conta += 1;
    nova_conta = dict(agencia=agencia, num_conta=num_conta, cpf=cpf_usuario)
    lista_contas.append(nova_conta)
    print("Conta adicionada com sucesso")
    return num_conta

#---------------------------------------------------------------------------------------------------------
# Função lista_usuarios
def lista_usuarios(*, lista_usuarios):
    if (len(lista_usuarios) < 1):
        print("Nenhum usuário encontrado")
        return
    if (len(lista_usuarios) == 1):
        print(f'1 usuário encontrado')
    else:
        print(f'{len(lista_usuarios)} usuários encontrados')
    for item in lista_usuarios:
        print("------------------")
        print(f'CPF: {item.get("cpf")}')
        print(f'Nome: {item.get("nome")}')
        print(f'Data de Nascimento: {item.get("nascimento")}')
        print(f'Endereço: {item.get("endereco")}')
        print("")

#---------------------------------------------------------------------------------------------------------
# Função lista_contas
def lista_contas(*, lista_contas):
    if (len(lista_contas) < 1):
        print("Nenhuma conta encontrada")
        return
    if (len(lista_contas) == 1):
        print(f'1 conta encontrada')
    else:
        print(f'{len(lista_contas)} contas encontradas')
    for item in lista_contas:
        print("------------------")
        print(f'Agência: {item.get("agencia")}')
        print(f'Número da Conta: {item.get("num_conta")}')
        print(f'CPF do usuário: {item.get("cpf")}')
        print("")

#---------------------------------------------------------------------------------------------------------
# -------------------- Main loop --------------------
#---------------------------------------------------------------------------------------------------------
while (True):

    opcao = input(menu)

    if (opcao == "d"):
        print("Entre com o valor a ser depositado: ", end="")
        valor = float(input())
        #saldo, extrato = deposito(saldo, valor, operacoes)
        saldo = deposito(saldo, valor, operacoes)
    
    elif (opcao == "s"):
        print("Entre com o valor a ser sacado: ", end="")
        valor = float(input())
        saldo, saque_numero = saque(saldo=saldo, valor=valor, extrato=operacoes, limite=LIMITE_SAQUE, numero_saques=saque_numero, limite_saques=LIMITE_NUM_SAQUES)

    elif (opcao == "e"):
        extrato_conta(saldo, extrato=operacoes)

    elif (opcao == "nu"):
        print("Entre com o CPF: ", end="")
        cpf = int(input())
        if busca_usuario_cpf(lista_usuarios=usuarios, cpf=f'{cpf}') >= 0:
            print("CPF já cadastrado. Operação cancelada.")
            continue
        print("Entre com o nome do usuário: ", end="")
        nome = input()
        print("Entre com a data de nascimento do usuário: ", end="")
        nascimento = input()
        print("Entre com o logradouro: ", end="")
        logradouro = input()
        print("Entre com o número do endereço: ", end="")
        numero = input()
        print("Entre com o bairro: ", end="")
        bairro = input()
        print("Entre com a cidade: ", end="")
        cidade = input()
        print("Entre com o estado (sigla): ", end="")
        estado = input()

        criar_usuario(lista_usuarios=usuarios, nome=nome, nascimento=nascimento, cpf=f'{cpf}', ender_logradouro=logradouro, ender_num=numero, ender_bairro=bairro, ender_cidade=cidade, ender_estado=estado)

    elif (opcao == "nc"):
        print("Entre com o CPF do dono da nova conta: ", end="")
        cpf = int(input())
        if busca_usuario_cpf(lista_usuarios=usuarios, cpf=f'{cpf}') < 0:
            print("CPF não encontrado. Operação cancelada.")
            continue       
        num_contas_total = criar_conta(lista_contas=contas, agencia=NUM_AGENCIA, num_conta=num_contas_total, cpf_usuario=cpf) 

    elif (opcao == "lu"):
        lista_usuarios(lista_usuarios=usuarios)

    elif (opcao == "lc"):
        lista_contas(lista_contas=contas)
            
    elif (opcao == "q"):
        print("Fim da operação")
        break

    else:
        print("Opção inválida")


