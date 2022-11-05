manha=[]
tarde=[]
noite=[]
lotacao_manha = 0
lotacao_tarde = 0
lotacao_noite = 0
retornar="s"
 
print("Reservas do Show do CBJR \o/")
 
#Pedindo para o usuário definir a configuração da matriz:
fileiras = int(input('Quantas fileiras a casa de show terá? '))
cadeiras = int(input('Quantas cadeiras cada fileira da casa de show terá? '))

#Instanciando as linhas da matriz
for i in range(0, fileiras, 1):
    manha.append([])
    tarde.append([])
    noite.append([])

#Instanciando as colunas dentro das linhas da matriz:
for l in range(0, fileiras, 1):
    for c in range(0, cadeiras, 1):    
        manha[l].append("vazio")
        tarde[l].append("vazio")
        noite[l].append("vazio")

#Enquanto o usuário desejar realizar uma nova consulta:
while(retornar=="s"):
    nome = input("Digite o seu nome: ")
    sessao = int(input("Digite a sessão que você deseja fazer a reserva (1-Manha, 2-Tarde, 3-Noite): "))
    fileira = int(input("Digite a fileira que você deseja sentar (1 até " + str(fileiras) + "): ")) - 1
    cadeira = int(input("Digite a cadeira que você deseja sentar (1 até " + str(cadeiras) + "): ")) - 1

    #Certificando que a quantidade de pessoas cadastradas é menor que 4/5 da lotação total:
    while((sessao == 1) and (lotacao_manha >= ((fileiras * cadeiras)*0.80) ) ):
        print('Sessao lotada, escolha outra sessão!')
        sessao = int(input("Digite a sessão que você deseja fazer a reserva (1-Manha, 2-Tarde, 3-Noite): "))
 
    while((sessao == 2) and (lotacao_tarde >= ((fileiras * cadeiras)*0.80) ) ):
        print('Sessao lotada, escolha outra sessão!')
        sessao = int(input("Digite a sessão que você deseja fazer a reserva (1-Manha, 2-Tarde, 3-Noite): "))
 
    while((sessao == 3) and (lotacao_noite >= ((fileiras * cadeiras)*0.80) ) ):
        print('Sessao lotada, escolha outra sessão!')
        sessao = int(input("Digite a sessão que você deseja fazer a reserva (1-Manha, 2-Tarde, 3-Noite): "))

    #Caso o usuário escolha o periodo da manhã:
    if (sessao == 1):
        #Se a posição da matriz tiver algo diferente de vazio, ela está ocupada:
        while (manha[fileira][cadeira] != "vazio"):
            print("Esse assento já está reservado!")
            fileira = int(input("Digite a fileira que você deseja sentar (1 até " + str(fileiras) + "): ")) - 1
            cadeira = int(input("Digite a cadeira que você deseja sentar (1 até " + str(cadeiras) + "): ")) - 1

        #Caso a posição tiver "vazio", está disponível para cadastro
        manha[fileira][cadeira] = nome
        lotacao_manha = lotacao_manha + 1

    #Período da tarde
    elif (sessao == 2):
        while (tarde[fileira][cadeira] != "vazio"):
            print("Esse assento já está reservado!")
            fileira = int(input("Digite a fileira que você deseja sentar (1 até " + str(fileiras) + "): ")) - 1
            cadeira = int(input("Digite a cadeira que você deseja sentar (1 até " + str(cadeiras) + "): ")) - 1
 
        tarde[fileira][cadeira] = nome
        lotacao_tarde = lotacao_tarde + 1

    #Período da noite
    else:
        while (noite[fileira][cadeira] != "vazio"):
            print("Esse assento já está reservado!")
            fileira = int(input("Digite a fileira que você deseja sentar (1 até " + str(fileiras) + "): ")) - 1
            cadeira = int(input("Digite a cadeira que você deseja sentar (1 até " + str(cadeiras) + "): ")) - 1
        noite[fileira][cadeira] = nome
        lotacao_noite = lotacao_noite + 1
 
    print("Reserva realizada com sucesso!")

    #Caso todas as sessões estejam lotadas, acontece um break para eu sair do looping porque não tenho mais lugar para cadastrar:
    if ( (lotacao_manha >= ((fileiras * cadeiras)*0.80) ) and
         (lotacao_tarde >= ((fileiras * cadeiras)*0.80) ) and
         (lotacao_noite >= ((fileiras * cadeiras)*0.80) ) ):
        print("Todas as sessões estão lotadas!")
        break
    #Caso ainda tenha lugar em pelo menos uma sessão, pergunto se o usuário deseja realizar uma nova consulta:
    else:
        retornar = input("Deseja realizar mais alguma reserva? (S/N)")

#Print do cadastro final
print("Mapa das reservas do show separados por período:")
#MANHA
print("Reservas da Manhã")
for i in range(0, fileiras, 1):
    print(manha[i])
#TARDE
print("Reservas da Tarde")
for i in range(0, fileiras, 1):
    print(tarde[i])
#NOITE
print("Reservas da Noite")
for i in range(0, fileiras, 1):
    print(noite[i])