clientes=[]
emails = set()

print('Cadastro de Clientes')

while(True):
    print('1 - Incluir')
    print('2 - Atualizar')
    print('3 - Excluir')
    print('4 - Exibir')
    print('5 - Sair')
    opcao = int(input('Digite a opção escolhida: '))

    if (opcao == 1):
        nome = input('Digite o seu nome: ')
        email = input('Digite a seu email: ')

        while (email in emails):
            print('Esse email já faz parte de outro cadastro. Escolha outro')
            email = input('Digite a seu email: ')
        emails.add(email)

        idade = int(input('Digite a sua idade: '))

        possuiConta = input('Possui conta bancária? (S/N): ')
        
        if (possuiConta == 'S'):
            agencia = input('Digite a sua agencia: ')
            numero = input('Digite o seu número: ')
            conta = (agencia, numero)
        else:
            conta = ()

        cliente = [nome, email, idade, conta]

        clientes.append(cliente)
    elif (opcao == 2):
        for cli in clientes:
            print(f'Nome: {cli[0]} - Email: {cli[1]} - Idade: {cli[2]}' )
            if (len(cli[3]) > 0):
                print(f'Agencia: {cli[3][0]} - Numero: {cli[3][1]}')
            else:
                print('Não possui conta')

    elif (opcao == 4):
        for cli in clientes:
            print(f'Nome: {cli[0]} - Email: {cli[1]} - Idade: {cli[2]}' )
            #if (len(cli[3]) > 0) ou if (cli[3]):
            if (len(cli[3]) > 0):
                print(f'Agencia: {cli[3][0]} - Numero: {cli[3][1]}')
            else:
                print('Não possui conta')
    else:
        break