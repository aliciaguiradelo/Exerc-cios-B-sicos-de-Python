#Importando biblioteca 'requests' para podermos fazer requisições e consumir uma API. Importei tbm a biblioteca datetime para poder utilizar seus métodos para formatar a data no formato dd/mm/aaaa
import requests
from datetime import datetime
FORMATO_DATA = '%d/%m/%Y'
# Faz a requisição da API e armazena os dados na variável feriados
response = requests.get('https://brasilapi.com.br/api/feriados/v1/2023')
feriados = response.json()

# Função para exibir a lista de feriados
def listar_feriados():
    print('Lista dos Feriados:')
    #Utilizando estrutura for para varrer a lista de feriados e enumerá-los um a um. Utilizei método strptime (atributo, formato desejado) para formatar a data. Método enumerate para informar a posição e valor.
    for i, feriado in enumerate(feriados):
        data = datetime.strptime(feriado['date'], '%Y-%m-%d')
        data_formatada = data.strftime(FORMATO_DATA)
        print(f'{i+1} - {data_formatada} - {feriado["name"]}')
    print('\n')

# Função para ver detalhes de um feriado específico. Mostra nome, tipo do feriado e os comentários.
def ver_detalhes():
    id_feriado = int(input('Digite o id do feriado: '))
    feriado = feriados[id_feriado-1]
    print(f'Descrição do feriado:{feriado["name"]}  -  Tipo: {feriado["type"]}')
    comentarios = feriado.get('comentarios', [])
    if comentarios:
        print('Comentários:')
        for i, comentario in enumerate(comentarios):
            print(f'{i+1} - NOME: {comentario["nome"]}  - TEXTO: {comentario["texto"]}')
    else:
        print('Não há comentários sobre esse feriado.')
    print('\n')

# Função para adicionar um comentário a um feriado
def adicionar_comentario():
    id_feriado = int(input('Digite o id do feriado: '))
    nome = input('Digite o seu nome: ')
    texto = input('Digite o seu comentário: ')
    comentario = {'nome': nome, 'texto': texto}
    if 'comentarios' in feriados[id_feriado-1]:
        feriados[id_feriado-1]['comentarios'].append(comentario)
    else:
        feriados[id_feriado-1]['comentarios'] = [comentario]
    print('Comentário adicionado com sucesso.\n')

# Função para excluir um comentário
def excluir_comentario():
    id_feriado = int(input('Digite o id do feriado: '))
    comentarios = feriados[id_feriado-1].get('comentarios', [])
    if comentarios:
        print('Comentários:')
        for i, comentario in enumerate(comentarios):
            print(f'{i+1} - NOME: {comentario["nome"]}  - TEXTO: {comentario["texto"]}')
        id_comentario = int(input('Digite o id do comentário que deseja excluir: '))
        if id_comentario <= len(comentarios):
            del comentarios[id_comentario-1]
            print('Comentário excluído com sucesso.\n')
        else:
            print('Comentário não encontrado.\n')
    else:
        print('Não há comentários sobre esse feriado.\n')

# Loop principal do programa
while True:
    print(listar_feriados())
    print('Escolha uma opção:')
    print('1 - Ver detalhes do feriado')
    print('2 - Fazer um comentário do feriado')
    print('3 - Excluir um comentário')
    print('4 - Listar feriados')
    print('0 - Sair')
    opcao = int(input())
    print('\n')
    if opcao == 1:
        ver_detalhes()
    elif opcao == 2:
        adicionar_comentario()
    elif opcao == 3:
        excluir_comentario()
    elif opcao == 4:
        listar_feriados()
    elif opcao == 0:
        break
    else:
        print('Opção inválida. Tente novamente.\n')