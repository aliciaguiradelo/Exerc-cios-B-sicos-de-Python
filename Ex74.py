cadastro = []

while True:
    nome = input("Digite o nome do produto: ")
    preco = input("Digite o preco do produto: ")
    qntd = input("Digite a quantidade do produto: ")

    produto = {"nome": nome, "preco": preco, "quantidade": qntd}

    while True:
        nomeLoja = input("Digite o nome da loja: ")
        cidade = input("Digite sua cidade: ")

        loja = [
            {"Nome da loja": nomeLoja, "Cidade": cidade}
        ]

        produto.update({'LOJAS': loja})

        cadastro.append(produto)

        maisLoja = input("Deseja cadastrar mais uma loja? (S/N) .. ")
        if maisLoja.upper() == "N":
                break

    print(cadastro)
    print ("-----------------")

    continuar = input("Deseja continuar (S/N)? ")
    if continuar.upper() == "N":
        break
print(cadastro)
print ("-----------------")