#Exemplo 01 - Chamando função com parâmetros por posição
def exibirMensagem():
    return 'Olá pessoal!'
print(exibirMensagem())

#Exemplo 02
def calcularDivisao(a, b):
    valor1 = float(a)
    valor2 = float(b)
    resultado = valor1 / valor2
    return resultado
v1 = float(input('Digite o primeiro valor: '))
v2 = float(input('Digite o segundo valor: '))
print('O resultado é: ', calcularDivisao(v1, v2))

#Exemplo 03 - Chamando função com parâmetros nomeados
def calcularDivisao(a, b):
    valor1 = float(a)
    valor2 = float(b)
    resultado = valor1 / valor2
    return resultado
v1 = float(input('Digite o primeiro valor: '))
v2 = float(input('Digite o segundo valor: '))
print('O resultado é: ', calcularDivisao(b = v2, a = v1))

#Exemplo 04 - Chamando função em arquivos diferentes
#Arquivo FuncoesUteis.py
def calcular_media(a, b):
    res = ( float(a) + float(b) ) / 2
    return res
#Arquivo Programa.py
import FuncoesUteis as fu
nota1 = float(input('Digite a nota da P1: '))
nota2 = float(input('Digite a nota da P2: '))
print(f'O resultado é {fu.calcular_media(nota1, nota2)}')