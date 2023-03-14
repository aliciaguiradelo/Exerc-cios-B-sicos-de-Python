def CadastrarPessoas(pessoa):
    nome = input ("Digite o nome: ")
    idade = int (input ("Digite a idade: "))
    cep = input("Digite seu CEP: ")
    numero = int (input ("Digite o número: "))
    complemento = int (input ("Digite o complemento: "))

def exibirPessoas (pessoa):
    for pessoa in listaPessoas:
        print(f"\n\nId: {pessoa['id']} \nNome: {pessoa['nome']} \nEndereço: {pessoa['logradouro']}\n\n")

def exibirEndereco (cep):