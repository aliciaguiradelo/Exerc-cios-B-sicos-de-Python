matriz = []

print("Determine o formato da matriz ")
linhas = int(input("Digite o número de linhas: "))
colunas=int(input("Digite o número de colunas: "))

for i in range (0,linhas,1):
    matriz.append([])

for l in range (0,linhas,1):
    for c in range (0,colunas, 1):
        nome=input("Digite um nome")
        matriz[i].append(nome)

print(matriz)

for i in range(0,linhas,1):
    print(matriz[i])

for l in range (0,linhas,1):
    for c in range (0,colunas, 1):
        print(matriz[l][c])