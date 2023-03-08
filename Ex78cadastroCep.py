#Importando biblioteca para trabalhar com API
import requests
#Criando ArrayList para armazenar o cadastro das pessoas
ListaPessoas = []

while True:
    #Definindo funções
    def exibirPessoas (pessoa):
        for pessoa in listaPessoas:
            print(f"\n\nId: {pessoa['id']} \nNome: {pessoa['nome']} \nEndereço: {pessoa['logradouro']}\n\n")
    print("Cadastro de Pessoas")
    print("\n1 - Incluir \n2 - Alterar \n3 - Excluir \n4 - Exibir \n5 - Sair \n")
    opcao = int(input("Digite a opção desejada: "))

    if (opcao == 1):
        nome = input ("Digite o nome: ")
        idade = int (input ("Digite a idade: "))
        cep = input("Digite seu CEP: ")
        numero = int (input ("Digite o número: "))
        complemento = int (input ("Digite o complemento: "))

        url = f"https://viacep.com.br/ws/{cep}/json/"

        response = requests.get(url)

        if response.status_code == 200:
            dados = response.json()
            print("\n\nNome: ",nome)
            print("Idade: ",idade)
            print(f"CEP: {dados['cep']}")
            print(f"Logradouro: {dados['logradouro']}")
            print("Número: ",numero)
            print("Complemento: ",complemento)
            print(f"Bairro: {dados['bairro']}")
            print(f"Cidade: {dados['localidade']}")
            print(f"Estado: {dados['uf']}")

            pessoa = {"Nome": nome, "Idade": idade, "Cep": {dados['cep']}, "Logradouro": {dados['logradouro']}, "Número": numero, "Complemento":complemento, "Bairro": {dados['bairro']}, "Cidade": {dados['localidade']}, "Estado": {dados['uf']}}

            ListaPessoas.append(pessoa)

            print("Pessoa cadastrada com sucesso!!")
        else:
            print("CEP não encontrado.")

    elif (opcao == 2):
        print(exibirPessoas(pessoa))
        nomePessoa = input ("Digite o nome que deseja alterar: ")
        idade = int (input ("Digite a nova idade: "))
        cep = input("Digite seu novo CEP: ")
        numero = int (input ("Digite o novo número: "))
        complemento = int (input ("Digite o novo complemento: "))

        url = f"https://viacep.com.br/ws/{cep}/json/"

        response = requests.get(url)

        if response.status_code == 200:
            dados = response.json()
            print("\n\nNome: ",nome)
            print("Idade: ",idade)
            print(f"CEP: {dados['cep']}")
            print(f"logradouro: {dados['logradouro']}")
            print("Número: ",numero)
            print("Complemento: ",complemento)
            print(f"Bairro: {dados['bairro']}")
            print(f"Cidade: {dados['localidade']}")
            print(f"Estado: {dados['uf']}")

            pessoa = {"Nome": nome, "Idade": idade, "Cep": {dados['cep']}, "Logradouro": {dados['logradouro']}, "Número": numero, "Complemento":complemento, "Bairro": {dados['bairro']}, "Cidade": {dados['localidade']}, "Estado": {dados['uf']}}

            for pessoa in ListaPessoas:
                if (pessoa['Nome'] == nomePessoa):
                    pessoa.update({'idade': idade})
                    pessoa.update({'cep': cep})
                    pessoa.update({'Logradouro': logradouro})
                    pessoa.update({'numero': numero})
                    pessoa.update({'complemento': complemento})
                    pessoa.update({'bairro': bairro})
                    pessoa.update({'cidade': localidade})
                    pessoa.update({'estado': uf})

            print("Pessoa atualizada com sucesso!!")
        else:
            print("CEP não encontrado.")

    elif (opcao == 3):
        print(exibirPessoas(pessoa))
        nomePessoa = input ("Digite o nome que deseja excluir: ")
        for pessoa in ListaPessoas:
            if (pessoa['Nome'] == nomePessoa):
                ListaPessoas.remove(pessoa)

    elif (opcao == 4):
        print(exibirPessoas(pessoa))
    else:
        break