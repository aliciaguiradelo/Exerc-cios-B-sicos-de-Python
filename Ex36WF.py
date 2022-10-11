x = int(input("Digite um número qualquer:"))

while (x<=0):
    print("Número inválido!")
    x = int(input("Digite outro número:"))
intervalo1 = int(input("Digite o primero valor do intervalo da tabuada:"))
intervalo2 = int(input("Digite o segundo valor do intervalo da tabuada:"))
while (intervalo1>intervalo2):
    print("Segundo intervalo inválido")
    intervalo2 = int(input("Digite o segundo intervalo novamente"))
for i in range(intervalo2,intervalo1-1,-1):
    t = x * i 
    print(f"{x} X {i} = {t}")
    i = i + 1