n = []

for i in range(0,20,1):
    x=int(input("Digite um número:"))
    n.append(x)
const=int(input("Digite uma constante multiplicativa:"))
for i in range(0,20,1):
    n[i]=n[i]*const
    print(n[i])
for x in n:
    print(x)
