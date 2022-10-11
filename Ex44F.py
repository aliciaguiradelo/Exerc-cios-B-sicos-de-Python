s=0
for i in range(1,11,1):
    numero=int(input("Digite um numero:"))
    while(numero<0):
        numero=int(input("Digite outro numero:"))
    if(i==1):
        maior=numero
    else:
        if (numero>maior):
            maior=numero
        s=s+numero
        media=s/10
print(s)
print(media)
