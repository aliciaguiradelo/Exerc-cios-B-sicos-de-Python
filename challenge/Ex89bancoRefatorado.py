import cx_Oracle

def connect_to_database():
    dsn = cx_Oracle.makedsn(host='oracle.fiap.com.br', port=1521, sid='ORCL')
    conn = cx_Oracle.connect(user='rm96960', password='180201', dsn=dsn)
    return conn

def include_student():
    conn = connect_to_database()
    cursor = conn.cursor()
    nome = input('Digite o seu nome: ')
    id = int(input('Digite seu ID: '))
    ra = int(input('Digite seu RA: '))
    curso = input('Digite o nome do curso: ')
    cursor.execute("INSERT INTO TB_ALUNO (ID, NOME, RA, CURSO) VALUES (:valor1, :valor2, :valor3, :valor4)",
                   valor1=id, valor2=nome, valor3=ra, valor4=curso)
    conn.commit()
    print('Registro incluído com sucesso!')
    cursor.close()
    conn.close()

def update_student():
    conn = connect_to_database()
    cursor = conn.cursor()
    id = int(input('Digite o ID que deseja atualizar: '))
    nome = input('Digite o novo nome: ')
    curso = input('Digite o novo curso: ')
    cursor.execute("UPDATE TB_ALUNO SET NOME=:valor1, CURSO=:valor2 WHERE ID=:valor3",
                   valor1=nome, valor2=curso, valor3=id)
    conn.commit()
    print('Registro alterado com sucesso!')
    cursor.close()
    conn.close()

def delete_student():
    conn = connect_to_database()
    cursor = conn.cursor()
    id = int(input('Digite o ID que deseja excluir: '))
    cursor.execute("DELETE FROM TB_ALUNO WHERE ID=:valor1", valor1=id)
    conn.commit()
    print('Registro excluído com sucesso!')
    cursor.close()
    conn.close()

def list_all_students():
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM TB_ALUNO')
    rows = cursor.fetchall()
    for row in rows:
        print(row)
        print(f'Id: {row[0]}')
        print(f'Nome: {row[1]}')
    cursor.close()
    conn.close()

def list_student():
    conn = connect_to_database()
    cursor = conn.cursor()
    id = int(input('Digite o ID que deseja listar: '))
    cursor.execute("SELECT * FROM TB_ALUNO WHERE ID=:valor1", valor1=id)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
        print(f'Id: {row[0]}')
        print(f'Nome: {row[1]}')
    cursor.close()
    conn.close()

while True:
    print('\n<<--Cadastro de Alunos-->>')
    print('\nEscolha uma opção:')
    print('1- Incluir Aluno')
    print('2- Alterar')
    print('3- Excluir')
    print('4- Listar alunos')
    print('5- Listar aluno')

    opcao = int(input('Digite a opção desejada: '))

    if opcao == 1:
        include_student()
    elif opcao == 2:
        update_student()
    elif opcao == 3:
        delete_student()
    elif opcao == 4:
        list_all_students()
    elif opcao == 5:
        list_student()
    else:
        print('Opção inválida')
