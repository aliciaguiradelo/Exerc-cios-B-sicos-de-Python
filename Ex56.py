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
    i=int(input("Dgite a idade: "))
    idade.append(i)

for i in range(0,3,1):
    print(f"{i + 1} pessoa: ")
    print("NOME:", nome[i])
    print("SEXO: ",sexo[i])
    print("IDADE: ", idade[i])