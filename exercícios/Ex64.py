par = []
impar = []
for i in range(0,10,1):
    x=int(input(f"Digite o {i + 1} valor :"))
    if(x % 2 == 0):
        par.append(x)
    else:
        impar.append(x)
        
for i in range(0,10,1):
    print("PARES : ", par[i])

for i in range(0,10,1):    
    print("IMPAR : ", impar[i])
print("PORCENTAGEM DE PARES", len(par) / (len(impar) + len(par)))
print("PORCENTAGEM DE ÍMPARES", len(impar) / (len(impar) + len(par)) )