a = float(input("Digite o primeiro lado do triângulo:"))
b = float(input("Digite o segundo lado do triângulo:"))
c = float(input("Digite o terceiro lado do triângulo:"))

if (a>b+c) or (b>a+c) or (c>a+b):
    print("Não é um triângulo")
elif (a*a==b*b+c*c) or (b*b==a*a+c*c) or (c*c==b*b+a*a):
    print("É um triângulo isósceles")
else:
    print("É um triângulo, mas não é isósceles")