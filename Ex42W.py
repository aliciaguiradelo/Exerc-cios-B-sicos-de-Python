cima=1
baixo=2
soma=0
n = int(input("Digite um valor n:"))
while((n<0) and (n>50)):
    print("Digite um valor n válido:")

cima=n
baixo=n+1
soma=(((1/2)+(cima/baixo))*n)/2
print("O termo", n, "é",cima, "/", baixo)
print("A soma é:", soma)