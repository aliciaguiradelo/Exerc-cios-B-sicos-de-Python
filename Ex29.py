a = float(input("Digite o primeiro valor:"))
b = float(input("Digite o segundo valor:"))
c = float(input("Digite o terceiro valor:"))

if (a>b) and (b>c):
  print("A sequência é:%.2f<%.2f<.2%f" %(a,b,c))
elif (a>c) and (c>b):
  print("A sequência é:%.2f<%.2f<%.2f" %(a,c,b))
elif (b>c) and (c>a):
  print("A sequência é:%.2f<%.2f<%.2f" %(b,c,a))
elif (b>a) and (a>c):
  print("A sequência é:%.2f<%.2f<%.2f" %(b,a,c))
elif (b>a) and (a>c):
  print("A sequência é:%.2f<%.2f<%.2f" %(a,b,c))
elif (c>a) and (a>b):
  print("A sequência é:%.2f<%.2f<%.2f" %(c,a,b))
else:
  print("A sequência é:%.2f<%.2f<%.2f" %(c,b,a))