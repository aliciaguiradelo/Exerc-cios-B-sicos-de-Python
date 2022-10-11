a = float(input("Digite o primeiro número:"))
b = float(input("Digite o segundo número:"))
c = float(input("Digite o terceiro número:"))

if (a==b==c):
  print("Os três números são iguais!")
elif (a>b) and (a>c):
  print("O maior valor é:", a)
elif (b>a) and (b>c):
  print("O maior valor é:", b)
else:
  print("O maior valor é:", c)
