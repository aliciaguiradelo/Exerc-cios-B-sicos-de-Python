pessoas = []

def cadastrar_pessoa():
    nome = input("Digite o nome da pessoa: ")
    email = input("Digite o email da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))

    conta = ()
    criar_conta = input("Deseja criar uma conta para essa pessoa? (s/n) ")
    if criar_conta.lower() == 's':
        agencia = input("Digite o número da agência: ")
        numero_conta = input("Digite o número da conta: ")
        saldo = float(input("Digite o saldo inicial: "))
        conta = (agencia, numero_conta, saldo)

    pessoa = [nome, email, idade, conta]
    pessoas.append(pessoa)

def listar_pessoas():
    for pessoa in pessoas:
        print(f"Nome: {pessoa[0]}\nEmail: {pessoa[1]}\nIdade: {pessoa[2]}")
        if pessoa[3]:
            print("Conta bancária:")
            print(f"Agência: {pessoa[3][0]}\nNúmero da conta: {pessoa[3][1]}\nSaldo: {pessoa[3][2]}")
        print()

def buscar_pessoa():
    nome = input("Digite o nome da pessoa que deseja buscar: ")
    for pessoa in pessoas:
        if pessoa[0] == nome:
            print(f"Nome: {pessoa[0]}\nEmail: {pessoa[1]}\nIdade: {pessoa[2]}")
            if pessoa[3]:
                print("Conta bancária:")
                print(f"Agência: {pessoa[3][0]}\nNúmero da conta: {pessoa[3][1]}\nSaldo: {pessoa[3][2]}")
            return
    print("Pessoa não encontrada.")

def atualizar_pessoa():
    nome = input("Digite o nome da pessoa que deseja atualizar: ")
    for pessoa in pessoas:
        if pessoa[0] == nome:
            email = input("Digite o novo email da pessoa: ")
            idade = int(input("Digite a nova idade da pessoa: "))
            pessoa[1] = email
            pessoa[2] = idade
            if pessoa[3]:
                atualizar_conta = input("Deseja atualizar a conta bancária dessa pessoa? (s/n) ")
                if atualizar_conta.lower() == 's':
                    saldo = float(input("Digite o novo saldo: "))
                    pessoa[3] = (pessoa[3][0], pessoa[3][1], saldo)
            print("Pessoa atualizada com sucesso.")
            return
    print("Pessoa não encontrada.")

def remover_pessoa():
    nome = input("Digite o nome da pessoa que deseja remover: ")
    for pessoa in pessoas:
        if pessoa[0] == nome:
            pessoas.remove(pessoa)
            print("Pessoa removida com sucesso.")
            return
    print("Pessoa não encontrada.")

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
        print("Encerrando o programa...")
        break

    else:
        print("Opção inválida. Tente novamente.")