pessoas = []

def cadastrar_pessoa():
    nome = input("Digite o nome da pessoa: ")
    email = input("Digite o email da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))

    conta = set()
    criar_conta = input("Deseja criar uma conta para essa pessoa? (s/n) ")
    if criar_conta.lower() == 's':
        agencia = input("Digite o número da agência: ")
        numero_conta = input("Digite o número da conta: ")
        saldo = float(input("Digite o saldo inicial: "))
        conta.add(agencia)
        conta.add(numero_conta)
        conta.add(saldo)

    pessoa = {"nome": nome, "email": email, "idade": idade, "conta": tuple(conta)}
    pessoas.append(pessoa)

def listar_pessoas():
    for pessoa in pessoas:
        print(pessoa)

def buscar_pessoa():
    nome = input("Digite o nome da pessoa que deseja buscar: ")
    for pessoa in pessoas:
        if pessoa["nome"] == nome:
            print(pessoa)
            break
    else:
        print("Pessoa não encontrada")

def atualizar_pessoa():
    nome = input("Digite o nome da pessoa que deseja atualizar: ")
    for pessoa in pessoas:
        if pessoa["nome"] == nome:
            print("Digite os novos dados da pessoa")
            novo_nome = input("Nome: ")
            novo_email = input("Email: ")
            nova_idade = int(input("Idade: "))

            conta = set(pessoa["conta"])
            if len(conta) > 0:
                print("A pessoa tem uma conta bancária")
                print("Digite os novos dados da conta bancária")
                novo_agencia = input("Agência: ")
                novo_numero_conta = input("Número da conta: ")
                novo_saldo = float(input("Saldo: "))
                conta.clear()
                conta.add(novo_agencia)
                conta.add(novo_numero_conta)
                conta.add(novo_saldo)

            pessoa["nome"] = novo_nome
            pessoa["email"] = novo_email
            pessoa["idade"] = nova_idade
            pessoa["conta"] = tuple(conta)

            print("Pessoa atualizada com sucesso")
            break
    else:
        print("Pessoa não encontrada")

def remover_pessoa():
    nome = input("Digite o nome da pessoa que deseja remover: ")
    for pessoa in pessoas:
        if pessoa["nome"] == nome:
            pessoas.remove(pessoa)
            print("Pessoa removida com sucesso")
            break
    else:
        print("Pessoa não encontrada")

def menu():
    print("\n**** CADASTRO DE PESSOAS ****")
    print("1 - Cadastrar pessoa")
    print("2 - Listar pessoas")
    print("3 - Buscar pessoa")
    print("4 - Atualizar pessoa")
    print("5 - Remover pessoa")
    print("0 - Sair")

while True:
    menu()
    opcao = input("Digite a opção desejada: ")
    if opcao == '1':
        cadastrar_pessoa()
    elif opcao == '2':
        listar_pessoas()
    elif opcao == '3':
        buscar_pessoa()
    elif opcao == '4':
        atualizar_pessoa()
    elif opcao == '5':
        remover_pessoa()
    elif opcao == '0':
        break
    else:
        print("Opção inválida")