rm = []
nome = []
curso = []

for i in range(0,3,1):
    n=(input(f"Digite o nome da {i + 1} pessoa :"))
    nome.append(n)

    r=(input(f"Digite o rm da {i + 1} pessoa : "))
    rm.append(r)
    
    c=(input(f"Digite o curso da {i + 1} pessoa : "))
    curso.append(c)

for i in range(0,3,1):
    print("NOME: ", nome[i])
    print("RM: ", rm[i])
    print("CURSO: ", curso[i])


