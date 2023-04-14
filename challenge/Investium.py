
listaCategoria = []
listaSetor = []

consulta="S"
id=0

def adicionarCategoria (id, nomeCategoria):

    #id += 1
    #id = id + 1

    categoria = {"id": id, "Nome da Categoria": nomeCategoria}

    listaCategoria.append(categoria)

    print("lista",listaCategoria)
    print("lista",categoria)

while(consulta=="S"):
    print("MENU DE FUNCIONALIDADES ADMINISTRADOR")
    print("1. Categoria do artigos \n"+
          "2. Setor da empresa \n")
    opcao=int(input("Digite a opção desejada: \n"))
    while (opcao>2) or (opcao<1):
        opcao=int(input("Digite uma opção válida: \n"))
    if (opcao==1):
        print(" ----- SUB-MENU ----- ")
        print("--- CATEGORIA ---")
        print("1 Adicionar \n"+
              "2 Editar \n"+
              "3 Excluir \n")
        subopcao=int(input("Digite o sub-menu desejado:  \n"))
        while(subopcao<1) or (subopcao>3):
            subopcao=int(input("Digite um sub-menu válido:  \n"))
        if(subopcao==1):
            nomeCategoria = input ("Digite o nome da categoria que deseja cadastrar: ")
            
            id = id + 1
            
            adicionarCategoria(id, nomeCategoria)
            
            print("lista",listaCategoria)


            
        elif(subopcao==2):
            #Print das categorias
            idCategoria = int ( input ("Digite o id da categoria que deseja editar: "))
            nomeCategoria = input ("Digite o novo nome: ")

            for cat in listaCategoria:
                categoria.update({"nomeCategoria":nomeCategoria})
                #if idCategoria==cat.id 
            print("lista",listaCategoria)
        else:
            #Print das categorias
            idCategoria = int ( input ("Digite o id da categoria que deseja excluir: "))
        consulta=input("Deseja realizar uma nova consulta? (S/N)").upper()
    elif(opcao==2):
        print(" ----- SUB-MENU ----- ")
        print(" --- SETOR DA EMPRESA --- \n")
        print("1 Adicionar \n"+
              "2 Editar \n"+
              "3 Excluir \n")
        subopcao=int(input("Digite o sub-menu desejado:  \n"))
        while(subopcao<1) or (subopcao>3):
            subopcao=int(input("Digite um sub-menu válido:  \n"))
        if(subopcao==1):
            nomeSetor = input ("Digite o nome do setor que deseja cadastrar: ")
        elif(subopcao==2):
            #Print das categorias
            idSetor = int ( input ("Digite o id do setor que deseja editar: "))
            nomeSetor = input ("Digite o novo nome: ")
        else:
            #Print das categorias
            idSetor = int ( input ("Digite o id do setor que deseja excluir: "))
        consulta=input("Deseja realizar uma nova consulta? (S/N)").upper()
    else:
        print("Opção inválida! ")
    consulta=input("Deseja realizar uma nova consulta? (S/N)").upper()
consulta="N"
print("Obrigada!")
print("-------------FIM DO PROGRAMA-------------")