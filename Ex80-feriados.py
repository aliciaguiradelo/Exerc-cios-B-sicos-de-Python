#Importanto biblioteca requests que é usada para enviar solicitações HTTP para servidores web e datetime que é usada para trabalhar com datas e horas em Python
import requests
from datetime import datetime

#A variável BASE_URL é definida como a URL base para a API de feriados do Brasil
BASE_URL = "https://brasilapi.com.br/api/feriados/v1/"

while True:
    #Criando função para buscar feriados
    def buscar_feriados(ano: int):
        url = BASE_URL + str(ano)
        response = requests.get(url)
        return response.json()

    def verificar_feriado(data: datetime):
        feriados = buscar_feriados(data.year)

        data_formatada = data.strftime("%Y-%m-%d")

        for item in feriados:
            print(data_formatada, item['date'])
            if data_formatada == item['date']:
                return item['name']

        return 'null'

    def feriados_do_mes(data: datetime):
        feriados = buscar_feriados(data.year)
        feriados_mes = []

        for dia in feriados:
            feriado_data = datetime.strptime(dia['date'], "%Y-%m-%d")
            if feriado_data.month == data.month:
                feriados_mes.append(f"{feriado_data.day}/{feriado_data.month} - {dia['name']}")

        return feriados_mes

    data_str = input("Digite uma data (dd/mm): ")

    data = datetime.strptime(f"2023-{data_str}", "%Y-%d/%m")

    feriado = verificar_feriado(data)
    if feriado != 'null':
        print(f"A data {data_str} é um feriado: {feriado}")
    else:
        print(f"A data {data_str} não é um feriado")

    feriados_mes = feriados_do_mes(data)
    if len(feriados_mes) > 0:
        print(f"Feriados do mês:")
        for feriado in feriados_mes:
            print(feriado)
    else:
        print("Não há feriados no mês")
    
    retorno = input ("Deseja realizar uma nova consulta (S/N)? ").upper()

    if retorno != "S":
        break
print("Fim do programa")