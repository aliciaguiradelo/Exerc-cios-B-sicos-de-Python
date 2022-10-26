matriz=[]
 
linhas = int(input('Digite a quantidade de linhas que a matriz terá: '))
colunas = int(input('Digite a quantidade de colunas que a matriz terá: '))

for i in range(0, linhas, 1):
    matriz.append([])

for l in range(0, linhas, 1):
    for c in range(0, colunas, 1):    
        num = int(input('Digite um numero: '))
        matriz[l].append(num)
 
for i in range(0, linhas, 1):
    print(matriz[i])

const=int(input("Digite uma constante multiplicativa: "))

for l in range(0, linhas, 1):
    for c in range(0, colunas, 1):
        matriz[l][c] = (matriz[l][c])*const

for i in range(0, linhas, 1):
    print(matriz[i])