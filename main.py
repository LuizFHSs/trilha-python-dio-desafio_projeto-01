import Modules.operacao_bancaria as ob

while True:

    menu = """\tBANCO DIO
    1 PARA DEPOSITAR
    2 PARA SACAR
    3 PARA EXIBIR EXTRATO
    4 PARA NOVO USUARIO
    5 PARA SAIR
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
        ob.criar_usuario()
    elif opcao == 5:
        break
    else:
        print("Opção Inválida!")
        break;
