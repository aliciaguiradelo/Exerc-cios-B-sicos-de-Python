cadastro = []

while True:
    nome = input("Digite o nome do cliente: ")
    idade = int(input("Digite a idade do cliente: "))
    profissao = input("Digite a profissao do cliente: ")
    salario = float(input("Digite o salário do cliente: "))

    cliente = {"nome": nome, "idade": idade, "profissao": profissao, "salario": salario}

    possuiConta = input ("O cliente possui conta bancária? (S/N) ").upper()

    if (possuiConta == "S"):
        while True:
            banco = int(input("Digite o numero do banco: "))
            agencia = int(input("Digite o numero da agencia: "))
            numero = int(input("Digite a profissao da conta: "))

            conta = [
                {"banco": banco, "agencia": agencia, "numero": numero}
            ]

            cliente.update({'conta': conta})

            cadastro.append(cliente)

            maisconta = input("Cadastrar mais uma conta (S/N)? ")
            if maisconta.upper() == "N":
                break

    elif (possuiConta=="N"):
        banco = ''
        agencia= ''
        numero = ''

        cliente.update({'conta': ''})

        cadastro.append(cliente)
    
    else:
        print("Digite uma responta válida! (S/N) ... ")
        possuiConta = input ("O cliente possui conta bancária? (S/N) ").upper()

    print(cadastro)
    print ("-----------------")

    continuar = input("Deseja continuar (S/N)? ")
    if continuar.upper() == "N":
        break
    #for cliente in cadastro:
    #    print(f"Nome": {cliente['nome']}  |  "Idade": {cliente['idade']}  |  "Profissao": {cliente['profissao']}  |  "Salário": {cliente['salario']}  |  "Conta": {cliente['conta']}  |  )
print(cadastro)
print ("-----------------")