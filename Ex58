nome = []
sexo = []
idade = []
qntd=0
qntd=int(input("Digite a quantidade de pessoas : "))
for i in range(0,qntd,1):
    n=input(f"Digite o nome da {i + 1} pessoa :")
    nome.append(n)

    s=input(f"Digite o sexo da {i + 1} pessoa : ").upper()
    while((s != "F") and (s!="M")):
        s=input("Digite uma inicial válida: ").upper()
    sexo.append(s)
    
    num=int(input(f"Digite a idade da {i + 1} pessoa : "))
    while(num<=0):
        num=int(input("Dgite uma idade válida: "))
    idade.append(num)

for i in range(0,qntd,1):
    if(idade[i]>18):
        print(f"POSIÇÃO : {i + 1}")
        print("NOME: ", nome[i])
        print("SEXO: ",sexo[i])
        print("IDADE: ", idade[i])
