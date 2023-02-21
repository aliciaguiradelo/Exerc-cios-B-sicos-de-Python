import requests

moedas = {
    "USD": "Dólar Americano",
    "EUR": "Euro",
    "JPY": "Iene Japonês",
    "GBP": "Libra Esterlina",
    "ARS": "Peso Argentino",
}

valor_em_reais = float(input("Digite o valor em reais: "))
moeda_de_destino = input(f"Digite a moeda de destino ({', '.join(moedas.keys())}): ").upper()

if moeda_de_destino in moedas:
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda_de_destino}-BRL"

    response = requests.get(url)
    if response.status_code == 200:
        dados = response.json()

        taxa_de_conversao = float(dados[f"{moeda_de_destino}BRL"]["ask"])
        valor_convertido = valor_em_reais / taxa_de_conversao

        nome_da_moeda = moedas.get(moeda_de_destino, "Moeda Desconhecida")
        print(f"R$ {valor_em_reais:.2f} equivale a {valor_convertido:.2f} {nome_da_moeda}")
    else:
        print("Conversão sem serviço!")
else:
    print("Moeda inválida!")