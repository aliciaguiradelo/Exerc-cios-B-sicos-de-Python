from re import I


matriz = [ [0,0,0,0], [0,0,0,0], [0,0,0,0] ]
 
for l in range(0, 3, 1):
    for c in range(0, 4, 1):
        matriz[l][c] = int(input('Digite um numero: '))
for i in range(0, 3, 1):
    print(matriz[i])
const=int(input("Digite uma constante multiplicativa: "))
for l in range(0, 3, 1):
    for c in range(0, 4, 1):
        matriz[l][c] = (matriz[l][c])*const
for i in range(0, 3, 1):
    print(matriz[i])