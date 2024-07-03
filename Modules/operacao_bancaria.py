# Listas
extratos = []
usuarios = []
contas_corrente = []

# Floats
saldo = 0.0

# Ints
contador_saque = 0

def deposito(valor_deposito):
    if valor_deposito > 0:
        global saldo
        saldo += valor_deposito
        extratos.append(f"Depósito de R$ {valor_deposito:.2f}")
    else:
        print("\nOperação falhou! valor informado é inválido.\n")

def saque(valor_saque):
    # 3 saques diarios
    # limite de 500 reais por saque
    LIMITE_SAQUE = 500
    global contador_saque
    global saldo
    if contador_saque < 3:
        if valor_saque <= saldo and valor_saque <= LIMITE_SAQUE:
            saldo -= valor_saque
            extratos.append(f"Saque de R$ {valor_saque:.2f}")
            contador_saque += 1
        else:
            print("\nOperação falhou! saldo insuficiente ou valor limite de saque ultrapassado!\n")
    else:
        print("\nOperação falhou! Limite de saque diário atendido.\n")

def extrato():
    if len(extratos) == 0:
        print("\nNão foram realizadas movimentações.\n")
    else:
        print()
        print("EXTRATO".center(22, '='))
        for saldos in range(len(extratos)):
            print(extratos[saldos])
        print(f"Saldo atual: R$ {saldo:.2f}")
        print("=".center(22, '='))
        print()

def novo_usuario():
    cadastrado = False

    cpf = input("Informe seu CPF (somente numeros): ")

    # Verificando na lista se já existe um cpf
    for _ in usuarios:
        if _.get("cpf") == cpf:
            cadastrado = True
            print("Usuário já cadastrado!")

    if not cadastrado:
        nome = input("Informe seu Nome: ")
        data_nascimento = input("Informe sua Data de Nascimento (dd-mm-aaaa): ")
        endereco = input("Informe seu Endereço (logradouro, nro - bairro - cidade/sigla estado): ")
        usuario = dict(cpf = cpf, nome = nome, data_nascimento = data_nascimento, endereco = endereco)
        usuarios.append(usuario)

def nova_conta_corrente():
    AGENCIA = "0001"
    numero_conta = len(contas_corrente) + 1
    existe_usuario = False

    print("\nNOVA CONTA CORRENTE DIO\n")
    cpf = input("Informe seu CPF: ")

    for _ in usuarios:
        if _.get("cpf") == cpf:
            existe_usuario = True
            conta_corrente = dict(agencia=AGENCIA, numero_conta=numero_conta, usuario=cpf)
            contas_corrente.append(conta_corrente)
    
    if not existe_usuario:
        print("Não é possível cria uma conta corrente, pois não existe um usuário com este CPF.")
        print("Cadastre um novo usuário para poder criar uma conta corrente!\n")