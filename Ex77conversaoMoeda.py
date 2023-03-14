#importando a biblioteca requests
import requests

#Input do valor em reais que será convertido
valor = float ( input ("Digite o valor em R$: "))

#Declarando varável moeda que vai especificar a busca da url
print("Deseja converter para:")
moeda = input ("Dólar  -  USD  \n" +
               "Euro   -  EUR  \n" +
               "Bitcoin-  BTC  \n").upper()

#Define a URL que será acessada pela variável chamada 'url'
url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"

#Usa a função get da biblioteca requests para realizar uma requisição HTTP GET para a variável URL; e armazena a resposta em uma variável chamada response.
response = requests.get(url)

#Verifica se a resposta HTTP de uma requisição anterior foi bem sucedida. 200 é o código de status para uma resposta bem sucedida. .status_code é um método que verifica o status de uma requisição HTTPS.
if response.status_code == 200:

    #Usa a função json() da biblioteca 'response' para decodificar a resposta HTTP em formato JSON e armazená-la na variável dados. Converte a resposta HTTPS (em formato JSON) obtida a partir da requisição anterior em  uma lista, um dicionário ou outros objetos Python, dependendo da estrutura de dados da resposta JSON original. Uma vez convertida em um objeto Python, a resposta pode ser manipulada e utilizada pelo código do programa para realizar diversas tarefas.
    dados = response.json()

    #Definindo a variável 'taxa' para receber o valor da taxa de conversão 'ask'. Porém, diferente dos outros exercícios, "ask" é um objeto que fica dentro de outro objeto "USD ou BTC"
    taxa = float(dados[f"{moeda}BRL"]["ask"])

    #Fazendo o cálculo da conversão, que pegando o valor inserido pelo usuário e dividindo pelo ask que foi recebido na api
    conversao = valor / taxa

    print(f"R$ {valor:.2f} equivale a {conversao:.2f} {moeda}")

#Caso o status não seja 200, ou seja, caso tenha sido mal sucedido
else:
    print("MOEDA não encontrada.")
