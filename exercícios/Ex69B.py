matriz1 = []
matriz2 = []

linhas=int(input("Digite o número de linhas da matriz: "))
colunas=int(input("Digite o número de colunas da matriz: "))

for i in range (0,linhas,1):
    matriz1.append([])

for l in range (0,linhas,1):
    for c in range (0,colunas,1):
        num=int(input("Digite um número: "))
        matriz1[l].append([num])
for i in range (0,linhas,1):
    print(matriz1[i])

const=int(input("Digite uma constante multiplicativa: "))

for i in range (0,linhas,1):
    matriz2.append([])

for l in range(0, linhas, 1):
    for c in range(0, colunas, 1):    
        matriz2[l][c] = matriz1[l].append(num*const)

#for l in range (0,linhas,1):
#    for c in range (0,colunas,1):
#        matriz2[l][c] = (matriz1[l][c])*const

for i in range (0,linhas,1):
    print(matriz2[i])