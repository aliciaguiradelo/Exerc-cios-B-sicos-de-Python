matriz1 = [ [0,0,0,0], [0,0,0,0], [0,0,0,0] ]
matriz2 = [ [0,0,0,0], [0,0,0,0], [0,0,0,0] ]

for l in range (0,3,1):
    for c in range (0,4,1):
        matriz1 [l][c] = int(input("Digite um número: "))
for i in range (0,3,1):
    print(matriz1[i])
const=int(input("Digite uma constante multiplicativa: "))
for l in range (0,3,1):
    for c in range (0,4,1):
        matriz2 [l][c] = (matriz1 [l][c])*const
for i in range(0,3,1):
    print(matriz2[i])