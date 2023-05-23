r="S"
while (r=="S"):

    n=int(input("Digite um numero:"))
    while(n<0):
        n=int(input("Digite outro numero:"))
    for i in range(n-1,0,-1):
        f = n*i
        n=f

    print(n)

    r=input("Você deseja realizar uma nova execução?(S/N):").upper()
    while(r!="S" and r!="N"):
        r=input("Digite uma resposta válida:").upper()