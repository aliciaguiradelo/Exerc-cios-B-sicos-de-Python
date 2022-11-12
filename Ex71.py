print("______RESERVA ÔNIBUS PARA LAS VEGAS______")

#Inicializando variáveis
onibus = []
retornar = "S"
lotacao = 0

#Instanciando as linhas da matriz:
for i in range (0,10,1):
    onibus.append([])

#Instanciando as colunas de array para cada linha de array:
for l in range(0,10,1):
    for c in range(0,4,1):
        onibus[l].append("-----")

#Enquanto o usuário quiser realizar um novo cadastro, o programa volta a partir desse ponto. Entrada de dados do usuário:
while (retornar=="S"):
    nome=input("Digite seu nome: ")
    fileira=int(input("Digite a fileira desejada (0 a 10): "))-1
    cadeira=int(input("Digite a cadeira desejada (0 a 4): "))-1

    #Garantindo que os valores de fileira e cadeira sejam válidos:
    while(fileira>10) or (fileira<0) or (cadeira>4) or (cadeira<0):
        fileira=int(input("Digite a fileira desejada (0 a 10): "))-1
        cadeira=int(input("Digite a cadeira desejada (0 a 4): "))-1
    
    #Caso o lugar escolhido esteja ocupado, receberá aviso:
    while(onibus[fileira][cadeira]!=("-----")):
        print=("Este lugar já está ocupado!")
        fileira=int(input("Digite a fileira desejada (0 a 10): "))-1
        cadeira=int(input("Digite a cadeira desejada (0 a 4): "))-1
    
    #Caso o lugar esteja vago, realizar reserva:
    onibus[fileira][cadeira]=nome
    lotacao=lotacao+1
    print("Reserva realizada com sucesso! ")
    for i in range(0,10,1):
        print(onibus[i])
    
    #Conferindo se ainda há vagas no ônibus:
    if(lotacao<41):
        retornar=input("Deseja realizar uma nova reserva? (S/N) ").upper()
    else:
        print("O ônibus está cheio! Bora! ")
        retornar="N"

#Caso o usuário não quiser realizar uma nova reserva, mostrar o mapa das posições:
print("Mapa das reservas do ônibus:")
for i in range(0,10,1):
    print(onibus[i])
print("Reservas concluídas com sucesso! ")