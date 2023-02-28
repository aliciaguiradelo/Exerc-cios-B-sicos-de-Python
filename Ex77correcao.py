import requests

moedas = {1: 'USD', 2: 'EUR', 3: 'BTC'}

print("Conversor de Moedas\n")

valor = float(input("Qual o valor em R$: "))
opcao = int(input("\nDeseja converter para: \n1 - Dólar \n2 - Euro \n3 - Bitcoin\n"))

url = f"https://economia.awesomeapi.com.br/json/last/{moedas[opcao]}-BRL"

response = requests.get(url)

if response.status_code == 200:
    dados = response.json()

valorConvertido = valor / float(dados[moedas[opcao]+"BRL"]['ask'])

print(f"O valor convertido em {moedas[opcao]} é: {valorConvertido:.2f}")