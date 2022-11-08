print("-------MAPA DE SALA------")

#Inicializando variáveis
sala = []
retornar = "S"
limite = 0

#Instanciando as linhas da matriz:
for i in range (0,8,1):
    sala.append([])

#Instanciando as colunas de array para cada linha de array:
for c in range(0,8,1):
    for f in range(0,5,1):
        sala[c].append("------")

#Enquanto o aluno quiser realizar uma nova consulta, o programa volta a partir desse ponto. Entrada de dados do usuário:
while (retornar=="S"):
    nome=input("Digite seu nome: ")
    fileira=int(input("Digite a fileira desejada (1 a 5): "))-1
    carteira=int(input("Digite a carteira desejada (1 a 8): "))-1

    #Garantindo que os valores de fileira e carteira sejam válidos:
    while(fileira>5) or (fileira<0) or (carteira>8) or (carteira<0):
        fileira=int(input("Digite a fileira desejada (1 a 5): "))-1
        carteira=int(input("Digite a carteira desejada (1 a 8): "))-1
    
    #Caso o lugar escolhido esteja ocupado, receberá aviso:
    while(sala[carteira][fileira]!=("------")):
        print=("Este lugar já está ocupado!")
        fileira=int(input("Digite a fileira desejada (1 a 5): "))-1
        carteira=int(input("Digite a carteira desejada (1 a 8): "))-1
    
    #Caso o lugar esteja vago, realizar reserva:
    sala[carteira][fileira]=nome
    limite=limite+1
    print("Reserva realizada com sucesso! ")
    for i in range(0,8,1):
        print(sala[i])
    
    #Conferindo se ainda há vagas no ônibus:
    if(limite<41):
        retornar=input("Deseja realizar uma nova consulta? (S/N) ").upper()
    else:
        print("O ônibus está cheio! Bora! ")

#Caso o aluno não quiser realizar uma nova consulta ao mapa da sala, mostrar o mapa das posições:
print("-------MAPA DE SALA------")
for i in range(0,8,1):
    print(sala[i])
print("Reservas concluídas com sucesso! ")