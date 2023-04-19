arquivo = open("C:\\Users\\USER\Desktop\\Lista-Compras-Fiap-Python", "r")
arquivo2 = open("C:\\Users\\USER\Desktop\\Lista-Compras-Fiap-Precos-Python", "w")
lines = arquivo.readlines()

for l in lines:
    produto = l.split(",")
    arquivo2.write(produto[0] + ",")
    total = float(produto[1]) * float(produto[2])
    arquivo2.write(f"{total}\n")