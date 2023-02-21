#importando a biblioteca requests
import requests

#Declarando varável login que vai especificar a busca da url
login = input("Digite o login que deseja consultar:  ")

#Define a URL que será acessada pela variável chamada 'url'
url = f"https://api.github.com/users/{login}"

#Usa a função get da biblioteca requests para realizar uma requisição HTTP GET para a variável URL; e armazena a resposta em uma variável chamada response.
response = requests.get(url)

#Verifica se a resposta HTTP de uma requisição anterior foi bem sucedida. 200 é o código de status para uma resposta bem sucedida. .status_code é um método que verifica o status de uma requisição HTTPS.
if response.status_code == 200:

    #Usa a função json() da biblioteca 'response' para decodificar a resposta HTTP em formato JSON e armazená-la na variável dados. Converte a resposta HTTPS (em formato JSON) obtida a partir da requisição anterior em  uma lista, um dicionário ou outros objetos Python, dependendo da estrutura de dados da resposta JSON original. Uma vez convertida em um objeto Python, a resposta pode ser manipulada e utilizada pelo código do programa para realizar diversas tarefas.
    dados = response.json()

    #Printando os dados obtidos da lista JSON
    print(f"LOGIN: {dados['login']}")
    print(f"SEGUINDO: {dados['following']}")
    print(f"SEGUIDORES: {dados['followers']}")
    print(f"REPOSITÓRIOS PÚBLICOS: {dados['public_repos']}")
    print(f"REPOSITÓRIOS PRIVADOS: {dados['hireable']}")

#Caso o status não seja 200, ou seja, caso tenha sido mal sucedido
else:
    print("LOGIN não encontrado.")