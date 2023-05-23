a = float(input("Digite o valor da aceleração em m/s^2:"))
v0 = float(input("Digite o valor da velocidade inicial do automóvel:"))
t = float(input("Digite o tempo de percurso do automóvel:"))

#Fórmula para o cálculo da velocidade:
v = v0 + (a*t)

#Estruturas de decisões
if (v<=40):
  print("Veículo muito lento.")
elif (40<v<=60):
  print("Velocidade permitida.")
elif (60<v<=80):
  print("Velocidade de cruzeiro.")
elif (80<v<=120):
  print ("Veículo rápido.")
else:
  print("Veículo muito rápido.")