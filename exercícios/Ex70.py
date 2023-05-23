matriz = []

retornar = "s"

linhas = int(input("Digite o número de linhas da matriz: "))

while(linhas>10):
    linhas = int(input("A matriz deve ter no máximo 10 linhas! Digite o número menor que 10: "))

colunas = int(input("Digite o número de colunas da matriz: "))

while(colunas>10):
    colunas = int(input("Digite o número menor que 10: "))

for i in range (0,linhas,1):
    matriz.append([])

for l in range (0,linhas,1):
    for c in range (0,colunas,1):
        matriz[l].append(int(input("Digite um número: ")))
        #num=int(input("Digite um número: "))
        #matriz[l].append([num])

for i in range(0,linhas,1):
    print(matriz[i])

while(retornar=="s"):
    localiza = int(input("Digite um número para ser localizado na matriz:"))

    res = ''

    for l in range(0, linhas,1):
        for c in range(0, colunas,1):
            if (matriz[l][c]==localiza):
                res = res + "[" + str(l) + "," + str(c) + "]"

    if(res ==""):
        print("O número " + str(localiza) + " não foi localizado!")
    else:
        print("O número " + str(localiza) + " foi localizado na posição: " + res)

    retornar=input("Deseja realizar uma nova consulta? (S/N)")