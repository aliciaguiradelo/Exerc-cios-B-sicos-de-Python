#Lista = [] apenas valor
#Tupla = () imutável, apenas valor
#Set = {} Não permite REPETIÇÃO, apenas valor
#Dicionário = {} chave - valor

#Criando uma lista clientes
clientes = []
#Criando um set para armazenar os emails que já foram cadastrados
email_cadastrado = set()

while True:
    print ("MENU: " +
           "\n1. Incluir"+
           "\n2. Atualizar"+
           "\n3. Excluir"+
           "\n4. Exibir"+
           "\n5. Sair")
    opcao = int (input ("Digite a opção desejada"))

    if (opcao==1):
        nome = input ("Digite o nome: ")
        email = input ("Digite o email: ")
        idade = int (input ("Digite o idade: "))

        while (email in email_cadastrado):
            print ("Esse email já está sendo usado em outro outro cadastro")
            email = input ("Digite outro email: ")

        #Depois de validar se esse email já foi cadastro e ter certeza que não foi, eu adiciono ele no SET que armazena emails cadatrados
        email_cadastrado.add(email)

        possuiConta = input ("Possui conta bancária? (S/N) ").upper()

        if(possuiConta=='S'):
            agencia = input ("Digite a agência: ")
            numero = input ("Digite o número: ")
            
            #Criando tupla para receber informações da conta
            conta = (agencia, numero)

        else:
            conta = ()

        #Criando lista para armazenar informações do cliente
        cliente = [nome, email, idade, conta]

        #Adicionando objeto do tipo cliente na lista
        clientes.append(cliente)

    elif (opcao == 2):
        for cli in clientes:
            print(f"Nome: {cli[0]} - Email: {cli[1]} - Idade: {cli[2]} ")
            if(len(cli[3])>0):
                print(f"Agência: {cli[3][0]} - Número: {cli[3][1]}")

    elif (opcao == 4):
        for cli in clientes:
            print(f"Nome: {cli[0]} - Email: {cli[1]} - Idade: {cli[2]} ")
            #if (len(cli[3]) > 0) ou if (cli[3]):
            if (len(cli[3])>0):
                print(f"Agencia: {cli[3][0]} - Numero: {cli[3][1]}")
            else:
                print("não possui conta ")
    else:
        break