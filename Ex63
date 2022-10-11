nome = []
sexo = []
idade = []

for i in range(0,3,1):
    n=(input(f"Digite o nome da {i + 1} pessoa :"))
    nome.append(n)

for i in range(0,3,1):
    s=(input("Digite o sexo: "))
    sexo.append(s)

for i in range(0,3,1):
    i=int(input(f"Digite a idade da {i+1} pessoa : "))
    idade.append(i)

for i in range(0,3,1):
    for j in range(i+1,3,1):
        if(idade[i]<idade[j]):
            aux= idade[j]
            idade[j] = idade[i]
            idade[i] = aux

for i in range(0,3,1):
    for j in range(i+1,3,1):
        if(sexo[i]<sexo[j]):
            aux= sexo[i]
            sexo[i] = sexo[j]
            sexo[j] = aux

for i in range(0,3,1):
    print("IDADE: ", idade[i])
for i in range(0,3,1):
    print("SEXO: ", sexo[i])