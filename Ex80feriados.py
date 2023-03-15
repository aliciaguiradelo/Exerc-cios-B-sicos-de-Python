import pip._vendor.requests as requests

listaFeriados=[]

dataInformada = input("Digite uma data dd/mm/yyyy: ")

url = "https://brasilapi.com.br/api/feriados/v1/2023"

response = requests.get(url)

if response.status_code == 200:
    dados = response.json()
    for feriado in dados:
        dataFormatada = feriado['date'][8:10] + "/" + feriado['date'][5:7] + "/" + feriado['date'][0:4]
        feriado.update({'date': dataFormatada})

        if (dataInformada[3:5] == feriado['date'][3:5]):
            feriadoMes = {'data':feriado['date'], 'nome': feriado['name']}
            listaFeriados.append(feriadoMes)

    if ( (len(listaFeriados) == 1) and (listaFeriados[0]['data'] == dataInformada)):
        print(f"A data que você digitou {dataInformada} é feriado - {listaFeriados[0]['nome']}")
    else:
        print('A data que você digitou não é feriado, mas temos todos esses no mês:')
        for fer in listaFeriados:   
            print(f"{fer['data']} - {fer['nome']}")