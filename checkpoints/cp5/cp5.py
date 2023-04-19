arquivo = open("C:\\.Facul\\CÓDIGOS\\BackEnd\\ExerciciosBasicosdePython\\checkpoints\\cp5\\lista_compras.txt", "a")
#Enquanto desejar cadastrar uma nova compra volta nessa linha
while True:
    try:
        #Insert dados do cliente
        nome = input("Digite o nome do cliente ")
        qntd = int (input("Deseja cadastrar quantos produtos? "))
        #Escreve no arquivo o nome do cliente e pula uma linha
        arquivo.write(nome + "\n")
        #Para cada produto que desejar comprar até chegar no número que o usuário digitou. Vai pulando de 1 em 1
        for i in range(0,qntd,1):
            #Para cada looping, escreve os dados do produto no arquivo
            arquivo.write(input("Digite o nome do produto:") + ",")
            arquivo.write(input("Digite a quantidade do produto:") + ",")
            arquivo.write(input("Digite o preco do produto:")+ "\n")
        #Valida se o usuário deseja fazer uma nova volta
        volta = input("Deseja cadastrar uma nova compra? (S/N)").upper()
        #Se ele não desejar, sai do looping
        if (volta == "N"):
            break
    except ValueError as e:
        print('Digitação de dados está incorreta! ')
    except IndexError as e:
        print('Índice está errado! ')
    except TypeError as e:
        print('Tipo de dado inserido está errado! ')
    except Exception as e:
        print('Erro, contate o adm do sistema - ' + str(e))
    else:
        print("Dados incluídos com sucesso! ")
#Fechando arquivo
arquivo.close()
#Abrindo arquivos
arquivo = open("C:\\.Facul\\CÓDIGOS\\BackEnd\\ExerciciosBasicosdePython\\checkpoints\\cp5\\lista_compras.txt", "r")
arquivo2 = open("C:\\.Facul\\CÓDIGOS\\BackEnd\\ExerciciosBasicosdePython\\checkpoints\\cp5\\lista_compras_total.txt", "a")
#Lê o conteúdo do arquivo e retorna uma Lista
lines = arquivo.readlines()
#Para cada compra vai somar valores totais
for i in range(0, len(lines), qntd+1):
    nome = lines[i].strip()
    #Para cada produto obter o valor "semi-total"
    for j in range(qntd):
        index = i + j + 1
        #Validando se o índice é menor que a quantidade de linhas
        if index < len(lines):
            #Lendo o arquivo 1 e retirando as vírgulas
            produto = lines[index].split(",")
            if len(produto) >= 2:
                #Atribuindo os valores para as variáveis
                nome_produto = produto[0]
                qntd_produto = float(produto[1])
                preco_produto = float(produto[2])
                total = qntd_produto * preco_produto
                #Escrevendo o resultado no arquivo2
            arquivo2.write(f"{nome},{nome_produto},{total:.2f}\n")
#Fechando arquivos
arquivo.close()
arquivo2.close()