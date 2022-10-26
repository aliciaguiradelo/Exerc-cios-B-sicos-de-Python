print("RESERVA ÔNIBUS PARA LAS VEGAS")

matriz = [ [0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0] ]

resposta = 'S'

while resposta == 'S':

    nome=input("Digite seu nome: ")

    fileira = int(input("Digite o número da fileira desejada: "))
    while(fileira>4):
        fileira = int(input("O ônibus possui apenas 4 fileiras. Digite um valor válido: : "))
    cadeira = int(input("Digite o número da cadeira desejada: "))
    while(cadeira>10):
        cadeira = int(input("O ônibus possui apenas 10 cadeiras por fileira. Digite um valor válido: "))

    for i in range (0,fileira,1):
        matriz.append([])

    for f in range (0,fileira,1):
        for c in range (0,cadeira,1):
            if( matriz[f][c] is None):
                matriz[fileira][cadeira]=nome
                for i in range(0,fileira,1):
                    print(matriz[i])
                
            else:
                print("Este assento está ocupado!")
            resposta = input("Você deseja reservar mais algum lugar? ").upper()
            resposta = resposta[0]
while resposta != "S" and resposta != "N" :
        resposta = input("Digite sim ou não. ").upper()
        resposta = resposta[0]
if resposta == "N":
        for f in range(0, fileira, 1):
            print(matriz[f])
