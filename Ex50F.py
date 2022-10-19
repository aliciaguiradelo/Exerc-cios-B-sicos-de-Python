a=int(input("Digite o início do intervalo:"))
b=int(input("Digite um numero:"))
while(a<0 and b<0):
    a=int(input("Digite outro numero:"))
    b=int(input("Digite outro numero:"))
for i in range(a,b + 1, 1):
    if(i % 2 == 0 and i > 10):
        print(f'{i}, ')