#importando a biblioteca requests
import requests

#Criando laço de repetição. Caso o usuário deseja realizar uma nova consulta, o código volta nesse ponto.
while True:
    #Declarando varável cep que vai especificar a busca da url
    dominio = input("Digite o domínio que deseja consultar: ")

    #Define a URL que será acessada pela variável chamada 'url'
    url = f"https://brasilapi.com.br/api/registrobr/v1/{dominio}"

    #Usa a função get da biblioteca requests para realizar uma requisição HTTP GET para a variável URL; e armazena a resposta em uma variável chamada response.
    response = requests.get(url)

    #Verifica se a resposta HTTP de uma requisição anterior foi bem sucedida. 200 é o código de status para uma resposta bem sucedida. .status_code é um método que verifica o status de uma requisição HTTPS.
    if response.status_code == 200:

        #Usa a função json() da biblioteca 'response' para decodificar a resposta HTTP em formato JSON e armazená-la na variável dados. Converte a resposta HTTPS (em formato JSON) obtida a partir da requisição anterior em  uma lista, um dicionário ou outros objetos Python, dependendo da estrutura de dados da resposta JSON original. Uma vez convertida em um objeto Python, a resposta pode ser manipulada e utilizada pelo código do programa para realizar diversas tarefas.
        dados = response.json()

        #Criando estrutura de decisão de acordo com o valor que será retornado pela API
        if (dados['status'] == "AVAILABLE"):
            #Caso o retorno da API seja AVAILABLE, ele vai printar a linha 23
            print ("Este domínio está disponível!!")
        else:
            #Caso o retorno seja REGISTRED, o programa vai printar a linha 27
            print (f"Esse domínio está ocupado e ficará disponível em {dados['expires-at']}")

    #Caso o status não seja 200, ou seja, caso tenha sido mal sucedido
    else:
        print("Domínio não encontrado.")

    #Definindo a variável retorno para receber a resposta se o usuário deseja realizar uma nova consulta.
    retorno = input ("Deseja realizar uma nova consulta? (SIM/NÃO) ").upper()

    #Caso o usuário digite qualquer coisa diferente de SIM, ele dá um break e sai do looping while True
    if retorno != "SIM":
        break

#Quando sair do looping vai printar a linha 41
print("Fim do programa")