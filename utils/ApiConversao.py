import requests
valor=''
def obterTaxa(moeda):
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
    response = requests.get(url)
    if response.status_code == 200:
        dados = response.json()
        return float(dados[f"{moeda}BRL"]["ask"])
    else:
        dados = ''
    return dados
def conversaoMoeda(valor,moeda):
    taxa = obterTaxa(moeda)
    valor_convertido = valor / taxa
    return valor_convertido