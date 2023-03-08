import requests

listaPessoas = []

while True:
    #Definindo funções
    def exibirPessoas (pessoa):
        for pessoa in listaPessoas:
            print(f"\n\nId: {pessoa['id']} \nNome: {pessoa['nome']} \nEndereço: {pessoa['logradouro']}\n\n")

    print("Cadastro de Pessoas")
    print("\n1 - Incluir \n2 - Alterar \n3 - Excluir \n4 - Exibir \n5 - Sair \n")
    opcao = int(input("Digite a opção desejada: "))

    if (opcao == 1):
        id = listaPessoas.__len__() + 1
        nome = input("Digite o nome: ")
        email = input("Digite a idade: ")
        cep = input("Digite o seu CEP: ")

        url = f"https://viacep.com.br/ws/{cep}/json/"   

        response = requests.get(url)

        if response.status_code == 200:
            dados = response.json()

        logradouro = dados['logradouro']
        bairro = dados['bairro']
        localidade = dados['localidade']
        uf = dados['uf']

        numero = input("Digite o número do endereço: ")
        complemento = input("Digite o complemento do endereço: ")

        pessoa = {"id": id, "nome": nome, "email": email, "logradouro": logradouro, "bairro": bairro, "localidade": localidade, "uf": uf, "numero": numero, "complemento": complemento }

        listaPessoas.append(pessoa)

        print('Pessoa cadastrada com sucesso!')

    elif (opcao == 2):
        print(exibirPessoas(pessoa))

        idPessoa = int(input('Digite o id da pessoa que deseja atualizar: '))
        nome = input('Digite o novo nome: ')
        email = input('Digite o novo email: ')

        for pessoa in listaPessoas:
            if (pessoa['id'] == idPessoa):
                pessoa.update({'nome': nome})
                pessoa.update({'email': email})

        print('Pessoa atualizada com sucesso!')
        
    elif (opcao == 3):
        print(exibirPessoas(pessoa))

        idPessoa = int(input('Digite o id da pessoa que deseja atualizar: '))

        for pessoa in listaPessoas:
            if (pessoa['id'] == idPessoa):
                listaPessoas.remove(pessoa)

    elif (opcao == 4):
        print(exibirPessoas(pessoa))
    else:
        break