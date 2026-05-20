from conta import Conta

minha_conta = Conta("Bob Esponja")
while True:
    print ("☠=== MENU ===☠")
    print ("[1] - DEPOSITAR")
    print ("[2] - SACAR")
    print ("[3] - CALCULAR RENDIMENTO")
    print ("[4] - MOSTRAR SALDO")
    print ("[5] - SAIR")
    
    opcao = input ("ESCOLHA UMA OPÇÃO: ")
    
    if opcao == "1":
        valor = float(input ("QUANTO DESEJA DEPOSITAR? "))
        minha_conta.depositar(valor)
        print ("DEPÓSITO FEITO ZÉ")
        
    elif opcao == "2":
        valor = float(input ("QUANTO DESEJA SACAR? "))
        minha_conta.sacar(valor)
        print ("SAQUE FEITO ZÉ")

    elif opcao == "3":
        rendimento = minha_conta.calcular_rendimento()
        print (f"RENDIMENTO: R${rendimento}")

    elif opcao == "4":
        minha_conta.mostrar_saldo()

    elif opcao == "5":
        print ("ENCERRANDO...")
        break

    else:
        print ("NÃO TEM ESSA NÃO JÃO ☠")

