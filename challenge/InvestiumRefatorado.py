import cx_Oracle

def connect_to_database():
    dsn = cx_Oracle.makedsn(host='oracle.fiap.com.br', port=1521, sid='ORCL')
    conn = cx_Oracle.connect(user='rm96384', password='200494', dsn=dsn)
    return conn

def cadastrar_categoria():
    conn = connect_to_database()
    cursor = conn.cursor()
    id = input('Digite o ID: ')
    descricao = input('Digite a descrição da categoria: ')
    cursor.execute("INSERT INTO CATEGORIA (ID_CAT, DESCRICAO) VALUES (:valor1, :valor2)",valor1=id, valor2=descricao)
    conn.commit()
    print('Registro incluído com sucesso!')
    cursor.close()
    conn.close()

def listar_categorias():
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM CATEGORIA')
    rows = cursor.fetchall()
    for row in rows:
        print(row)
        print(f'Id: {row[0]}')
        print(f'Descrição: {row[1]}')
    cursor.close()
    conn.close()
        
def atualizar_categoria():
    conn = connect_to_database()
    cursor = conn.cursor()
    id = input('Digite o ID que deseja atualizar: ')
    descricao = input('Digite a nova descrição: ')
    cursor.execute("UPDATE CATEGORIA SET DESCRICAO=:valor1 WHERE ID_CAT=:valor2",valor1=descricao, valor2=id)
    conn.commit()
    print('Registro alterado com sucesso!')
    cursor.close()
    conn.close()

def remover_categoria():
    conn = connect_to_database()
    cursor = conn.cursor()
    id = input('Digite o ID que deseja excluir: ')
    cursor.execute("SELECT * FROM CATEGORIA WHERE ID_CAT=:valor1", valor1=id)
    row = cursor.fetchone()
    if row is None:
        print('O ID informado não existe na tabela.')
    else:
        cursor.execute("DELETE FROM CATEGORIA WHERE ID_CAT=:valor1", valor1=id)
        conn.commit()
        print('Registro excluído com sucesso!')
    cursor.close()
    conn.close()
    
def cadastrar_setor():
    conn = connect_to_database()
    cursor = conn.cursor()
    id = input('Digite o ID: ')
    descricao = input('Digite a descrição do setor: ')
    cursor.execute("INSERT INTO SETOR (ID_SETOR, DESCRICAO) VALUES (:valor1, :valor2)",valor1=id, valor2=descricao)
    conn.commit()
    print('Registro incluído com sucesso!')
    cursor.close()
    conn.close()
    
def listar_setor():
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM SETOR')
    rows = cursor.fetchall()
    for row in rows:
        print(row)
        print(f'Id: {row[0]}')
        print(f'Descrição: {row[1]}')
    cursor.close()
    conn.close()

def atualizar_setor():
    conn = connect_to_database()
    cursor = conn.cursor()
    id = input('Digite o ID que deseja atualizar: ')
    descricao = input('Digite a nova descrição: ')
    cursor.execute("UPDATE SETOR SET DESCRICAO=:valor1 WHERE ID_SETOR=:valor2",valor1=descricao, valor2=id)
    conn.commit()
    print('Registro alterado com sucesso!')
    cursor.close()
    conn.close()

def remover_setor():
    conn = connect_to_database()
    cursor = conn.cursor()
    id = input('Digite o ID que deseja excluir: ')
    cursor.execute("SELECT * FROM SETOR WHERE ID_SETOR=:valor1", valor1=id)
    row = cursor.fetchone()
    if row is None:
        print('O ID informado não existe na tabela.')
    else:
        cursor.execute("DELETE FROM SETOR WHERE ID_SETOR=:valor1", valor1=id)
        conn.commit()
        print('Registro excluído com sucesso!')
    cursor.close()
    conn.close()

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
          "3 - Atualizar \n"+
          "4 - Remover \n"+
          "0 - Sair")
#Função do menu setor
def menu_setor():
    print("--- SETOR ---")
    print("1 - Adicionar \n"+
          "2 - Listar \n"+
          "3 - Atualizar \n"+
          "4 - Remover \n"+
          "0 - Sair")
#id=len(listaCategoria)
#id2=len(listaSetor)
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
        if subopcao == '1':
            cadastrar_categoria()
        elif subopcao == '2':
            listar_categorias()
        elif subopcao == '3':
            atualizar_categoria()
        elif subopcao == '4':
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
            cadastrar_setor()
        elif subopcao == '2':
            listar_setor()
        elif subopcao == '3':
            atualizar_setor()
        elif subopcao == '4':
            remover_setor()
        elif subopcao == '0':
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")
    #Opção inválida
    else:
        print("Opção inválida. Tente novamente.")