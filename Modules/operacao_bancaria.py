extratos = []
saldo = 0.0
contador_saque = 0

def deposito(valor_deposito):
    if valor_deposito > 0:
        global saldo
        saldo += valor_deposito
        extratos.append(f"Depósito de R$ {valor_deposito:.2f}")
    else:
        print("Operação falhou! valor informado é inválido.")

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
            print("Operação falhou! saldo insuficiente ou valor limite de saque ultrapassado!")
    else:
        print("Operação falhou! Limite de saque diário atendido.")

def extrato():
    if len(extratos) == 0:
        print("Não foram realizadas movimentações.")
    else:
        print()
        print("EXTRATO".center(22, '='))
        for saldos in range(len(extratos)):
            print(extratos[saldos])
        print(f"Saldo atual: R$ {saldo:.2f}")
        print("=".center(22, '='))
        print()
       