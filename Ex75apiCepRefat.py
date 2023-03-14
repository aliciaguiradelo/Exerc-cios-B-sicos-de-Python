from utils import ApiCep as ac
while True:
    cep = input("Digite o CEP desejado: ")
    dados = ac.ConsultarCep(cep)
    if (dados != ''):
        print(f"CEP: {dados['cep']}")
        print(f"Logradouro: {dados['logradouro']}")
        print(f"Bairro: {dados['bairro']}")
        print(f"Cidade: {dados['localidade']}")
        print(f"Estado: {dados['uf']}")
    else:
        print("CEP não encontrado.")
    retorno = input ("Deseja realizar uma nova consulta? S/N")
    if retorno == 'n':
        break
print("Obrigada!")