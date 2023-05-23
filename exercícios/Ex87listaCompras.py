arquivo = open("C:\\Users\\USER\Desktop\\Lista-Compras-Fiap-Python", "w")

for i in range(0,3,1):
    arquivo.write(input("Digite o nome do produto:") + ",")
    arquivo.write(input("Digite a quantidade do produto:") + ",")
    arquivo.write(input("Digite o preco do produto:")+ "\n")