numeros = []
for i in range(0,10,1):
    x=int(input("Digite um número:"))
    numeros.append(x)
print("Os números digitados foram:")

for i in range(9,-1,-1):
    print(numeros[i])
