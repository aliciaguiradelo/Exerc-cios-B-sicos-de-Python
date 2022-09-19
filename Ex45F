soma=0
menor=0
maior=0
positivos=0
negativos=0
qnt=int(input("Digite a quantidade de números:"))
while(qnt<0 and qnt<=20):
    i=int(input("Digite novamente:"))
for i in range(1,qnt+1,1):
    n=int(input("Digite um número:"))
    
    
    if(i==1):
        maior = n
        menor = n
    else:
        if(n>=maior):
            maior= n
        elif(n<=menor):
            menor=n
    
    if(n > 0):
        positivos = positivos + 1
    else:
        negativos = negativos + 1
    
    soma=soma+n
    media=soma/10
    porcentagemPositivo = (positivos * 100) / i
    porcentagemNegativo = (negativos * 100) / i
    


print("O maior é:", maior)
print("O menoré:", menor)
print("A soma é:", soma)
print("A média é:", media)
print("A porcentagem de positivos é:", porcentagemPositivo)
print("A porcentagem de negativos é:", porcentagemNegativo)
