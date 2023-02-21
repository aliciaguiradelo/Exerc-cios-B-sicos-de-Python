import requests

# Função que faz a busca na API de CEP e retorna as informações de endereço
def busca_cep(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'
    response = requests.get(url)
    if response.status_code == 200:
        dados = response.json()
        return {
            'rua': dados['logradouro'],
            'bairro': dados['bairro'],
            'cidade': dados['localidade'],
            'estado': dados['uf']
        }
    else:
        return None

cadastro = {}

while True:
    opcao = input("Digite a opção desejada (I - Incluir, A - Alterar, E - Excluir, C - Consultar, S - Sair): ").upper()
    
    if opcao == "I":
        nome = input("Nome: ")
        email = input("E-mail: ")
        cep = input("CEP: ")
        endereco = busca_cep(cep)
        if endereco is None:
            print("CEP inválido!")
        else:
            numero = input("Número da casa: ")
            complemento = input("Complemento: ")
            cadastro[email] = {
                'nome': nome,
                'endereco': endereco,
                'numero': numero,
                'complemento': complemento
            }
            print("Pessoa incluída com sucesso!")
    
    elif opcao == "A":
        email = input("E-mail da pessoa a ser alterada: ")
        if email in cadastro:
            nome = input("Novo nome: ")
            cep = input("Novo CEP: ")
            endereco = busca_cep(cep)
            if endereco is None:
                print("CEP inválido!")
            else:
                numero = input("Novo número da casa: ")
                complemento = input("Novo complemento: ")
                cadastro[email]['nome'] = nome
                cadastro[email]['endereco'] = endereco
                cadastro[email]['numero'] = numero
                cadastro[email]['complemento'] = complemento
                print("Dados da pessoa alterados com sucesso!")
        else:
            print("Pessoa não encontrada no cadastro!")
    
    elif opcao == "E":
        email = input("E-mail da pessoa a ser excluída: ")
        if email in cadastro:
            del cadastro[email]
            print("Pessoa excluída com sucesso!")
        else:
            print("Pessoa não encontrada no cadastro!")
    
    elif opcao == "C":
        email = input("E-mail da pessoa a ser consultada: ")
        if email in cadastro:
            print(f"Nome: {cadastro[email]['nome']}")
            print(f"Endereço: {cadastro[email]['endereco']['rua']}, {cadastro[email]['numero']}, {cadastro[email]['complemento']}, {cadastro[email]['endereco']['bairro']}, {cadastro[email]['endereco']['cidade']}, {cadastro[email]['endereco']['estado']}")
            print(f"Número da casa: {cadastro[email]['numero']}")
            print(f"Complemento da casa: {cadastro[email]['complemento']}")
    elif opcao == "S":
        break
    
    else:
        print("Opção inválida!")