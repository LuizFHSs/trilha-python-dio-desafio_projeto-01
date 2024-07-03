import Modules.operacao_bancaria as ob

while True:

    menu = """\tBANCO DIO
    1 PARA DEPOSITAR
    2 PARA SACAR
    3 PARA EXIBIR EXTRATO
    4 PARA NOVO USUARIO
    5 PARA NOVA CONTA CORRENTE
    6 PARA LISTAR USUARIOS
    7 PARA LISTAR CONTAS CORRENTE
    8 PARA SAIR
    """
    print(menu)
    opcao = int(input("Digite a opção: "))

    if opcao == 1:
        valor_deposito = float(input("Digite o valor do deposito: "))
        ob.deposito(valor_deposito)
    elif opcao == 2:
        valor_saque = float(input("Digite o valor do saque: "))
        ob.saque(valor_saque)
    elif opcao == 3:
        ob.extrato()
    elif opcao == 4:
        ob.novo_usuario()
    elif opcao == 5:
        ob.nova_conta_corrente()
    elif opcao == 6:
        for _ in ob.usuarios:
            print(_.get("nome"))
    elif opcao == 7:
        for _ in ob.contas_corrente:
            print(f"Conta: {_.get("numero_conta")}\tTitular: {_.get("usuario")}")
    elif opcao == 8:
        break
    else:
        print("Opção Inválida!")
        break;
