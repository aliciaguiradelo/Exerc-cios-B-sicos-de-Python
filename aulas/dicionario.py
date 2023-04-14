dados = []

while True:
    nome = input ("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    salario = float(input("Digite o salário: "))

    pessoa = {"nome": nome, "id": idade, "salario": salario}

    dados.append(pessoa)

    continuar = input("Deseja continuar (S/N)? ")
    if continuar.upper() == "N":
        break

for pessoa in dados:
    print(f"Nome: {pessoa['nome']} | Idade: {pessoa['idade']} | Salario: {pessoa['pessoa']}")