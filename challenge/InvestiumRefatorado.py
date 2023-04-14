#Lista pré-definida conforme o site
listaCategoria = [[1,"IPO"], 
                  [2, "Educação financeira"], 
                  [3, "Investimento"], 
                  [4, "Bolsa de valores"]]
listaSetor = [[1,"Alimentício"], 
              [2, "Bancário"], 
              [3, "Agronegócio"]]
#Funções (CRUD) para o menu Categoria dos artigos
#Create
def cadastrar_categoria():
    nomeCategoria = input("Digite o nome da nova categoria: ")
    #id = len(listaCategoria) + 1
    categoria = [id,nomeCategoria]
    listaCategoria.append(categoria)
#Read
def listar_categorias():
    for categoria in listaCategoria:
        print (f"ID : {categoria[0]}    -    NOME : {categoria[1]}")
        
def buscar_categoria():
    id = int(input("Digite o id da categoria que deseja buscar: "))
    categoria_encontrada = False
    for categoria in listaCategoria:
        if categoria[0] == id:
            print (f"ID : {categoria[0]}    -    NOME : {categoria[1]}")
            categoria_encontrada = True
            break
    if not categoria_encontrada:
        print("Categoria não encontrada.")
#Update
def atualizar_categoria():
    listar_categorias()
    id =int(input("Digite o id da categoria que deseja atualizar: "))
    categoria_encontrada = False
    for categoria in listaCategoria:
        if categoria[0] == id:
            print (f"ID : {categoria[0]}    -    NOME : {categoria[1]}")
            categoria_encontrada = True
            nomeCategoria = input("Digite o novo nome da categoria: ")
            categoria[1]=nomeCategoria
            break
    if not categoria_encontrada:
        print("Categoria não encontrada.")
#Delete
def remover_categoria():
    listar_categorias()
    id =int(input("Digite o id da categoria que deseja remover: "))
    categoria_encontrada = False
    for categoria in listaCategoria:
        if categoria[0] == id:
            print (f"ID : {categoria[0]}    -    NOME : {categoria[1]}")
            categoria_encontrada = True
            listaCategoria.remove(categoria)
            print("Categoria removida com sucesso.")
            break
    if not categoria_encontrada:
        print("Categoria não encontrada.")
#Funções (CRUD) para o menu Setor da empresas
#Create
def cadastrar_setor():
    nomeSetor = input("Digite o nome do novo setor: ")
    #id = len(listaSetor) + 1
    setor = [id2,nomeSetor]
    listaSetor.append(setor)
#Read
def listar_setor():
    for setor in listaSetor:
        print (f"ID :{setor[0]}    -    NOME : {setor[1]}")

def buscar_setor():
    id2 = int(input("Digite o id do setor que deseja buscar: "))
    setor_encontrado = False
    for setor in listaSetor:
        if setor[0] == id2:
            print (f"ID : {setor[0]}    -    NOME : {setor[1]}")
            setor_encontrado = True
            break
    if not setor_encontrado:
        print("Setor não encontrado.")
#Update
def atualizar_setor():
    listar_setor()
    id2 =int(input("Digite o id do setor que deseja atualizar: "))
    setor_encontrado=False
    for setor in listaSetor:
        if setor[0] == id2:
            print (f"ID : {setor[0]}    -    NOME : {setor[1]}")
            setor_encontrado=True
            nomeSetor = input("Digite o novo nome do setor: ")
            setor[1] = nomeSetor
            print("Setor atualizado com sucesso.")
            break
    if not setor_encontrado:
        print("Setor não encontrado.")
#Delete
def remover_setor():
    listar_setor()
    id2 =int(input("Digite o id do setor que deseja remover: "))
    setor_encontrado=False
    for setor in listaSetor:
        if setor[0] == id2:
            print (f"ID : {setor[0]}    -    NOME : {setor[1]}")
            setor_encontrado=True
            listaSetor.remove(setor)
            print("Setor removido com sucesso.")
            break
    if not setor_encontrado:
        print("Setor não encontrado.")
#Função do menu principal
def menu_principal():
    print("\n****   MENU DE FUNCIONALIDADES ADMINISTRADOR   ****")
    print("1 - Administrar categoria dos artigos")
    print("2 - Administrar setor das empresas")
#Função do menu categoria
def menu_categoria():
    print("--- CATEGORIA ---")
    print("1 - Adicionar \n"+
          "2 - Listar \n"+
          "3 - Buscar \n"+
          "4 - Atualizar \n"+
          "5 - Remover \n"+
          "0 - Sair")
#Função do menu setor
def menu_setor():
    print("--- SETOR ---")
    print("1 - Adicionar \n"+
          "2 - Listar \n"+
          "3 - Buscar \n"+
          "4 - Atualizar \n"+
          "5 - Remover \n"+
          "0 - Sair")
id=len(listaCategoria)
id2=len(listaSetor)
#Enquando o usuário desejar realizar uma nova consulta
#Se o usuário digitar 0, dá um break e sai do looping while True
while True:
    #Menu princial
    menu_principal()
    opcao = input("Digite a opção desejada: ")
    #Menu Categoria
    if opcao == '1':
        menu_categoria()
        subopcao = input("Digite a subopção desejada: ")
        #Create
        if subopcao == '1':
            id = id + 1
            cadastrar_categoria()
        #Read
        elif subopcao == '2':
            listar_categorias()
        #"Select"
        elif subopcao == '3':
            buscar_categoria()

        elif subopcao == '4':
            atualizar_categoria()

        elif subopcao == '5':
            remover_categoria()

        elif subopcao == '0':
            print("Encerrando o programa...")
            break

        else:
            print("Opção inválida. Tente novamente.")
    #Menu Setor
    elif opcao == '2':
        menu_setor()
        subopcao = input("Digite a subopção desejada: ")

        if subopcao == '1':
            id2 = id2 + 1
            cadastrar_setor()
        
        elif subopcao == '2':
            listar_setor()

        elif subopcao == '3':
            buscar_setor()

        elif subopcao == '4':
            atualizar_setor()

        elif subopcao == '5':
            remover_setor()

        elif subopcao == '0':
            print("Encerrando o programa...")
            break

        else:
            print("Opção inválida. Tente novamente.")
    #Opção inválida
    else:
        print("Opção inválida. Tente novamente.")