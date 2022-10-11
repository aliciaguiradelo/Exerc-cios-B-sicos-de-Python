a = float(input("Digite sua altura:"))
p = float(input("Digite seu peso:"))
g = str(input("Digite seu gênero:"))

imc = p/(a*a)

if (g=="masculino"):
    if (imc < 20):
        print("Abaixo")
    elif (imc < 25):
        print("Acima")
    else:
        print("Ideal")
else:
    if (imc < 19):
        print("Abaixo")
    elif (imc < 24):
        print("Acima")
    else:
        print("Ideal")
