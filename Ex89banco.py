import cx_Oracle

while True:
    print('\n<<--Cadastro de Alunos-->>')
    print('\nEscolha uma opção:')
    print('1- Incluir Aluno')
    print('2- Alterar')
    print('3- Excluir')
    print('4- Listar alunos')
    print('5- Listar aluno')

    opcao = int(input('Digite a opção desejada: '))

    if (opcao == 1):
        dsn = cx_Oracle.makedsn(host='oracle.fiap.com.br', port=1521, sid='ORCL')
        conn = cx_Oracle.connect(user='rm96960', password='180201', dsn=dsn)
        cursor = conn.cursor()
        nome = input('Digite o seu nome: ')
        id = int(input('Digite seu id: '))
        ra = int(input('Digite seu RA: '))
        curso = input('Digite o nome do curso: ')
        cursor.execute("INSERT INTO TB_ALUNO (ID, NOME, RA, CURSO) VALUES (:valor1, :valor2, :valor3, :valor4)", valor1=id, valor2=nome,valor3=ra, valor4=curso)
        conn.commit()
        print('Registro incluído com sucesso!')
        cursor.close()
        conn.close()

    elif (opcao == 2):
        dsn = cx_Oracle.makedsn(host='oracle.fiap.com.br', port=1521, sid='ORCL')
        conn = cx_Oracle.connect(user='rm96960', password='180201', dsn=dsn)
        cursor = conn.cursor()
        id = int(input('Digite o ID que deseja atualizar: '))
        nome = input('Digite o novo nome: ')
        curso = input('Digite o novo curso: ')
        cursor.execute("UPDATE TB_ALUNO SET NOME=:valor1, CURSO=:valor2 WHERE ID=:valor3", valor1=nome, valor2=curso, valor3=id)
        conn.commit()
        print('Registro alterado com sucesso!')
        cursor.close()
        conn.close()

    elif (opcao == 3):
        dsn = cx_Oracle.makedsn(host='oracle.fiap.com.br', port=1521, sid='ORCL')
        conn = cx_Oracle.connect(user='rm96960', password='180201', dsn=dsn)
        cursor = conn.cursor()
        id = int(input('Digite o ID que deseja excluir: '))
        cursor.execute("DELETE FROM TB_ALUNO WHERE ID=:valor1", valor1=id)
        conn.commit()
        print('Registro excluído com sucesso!')
        cursor.close()
        conn.close()

    elif (opcao == 4):
        dsn = cx_Oracle.makedsn(host='oracle.fiap.com.br', port=1521, sid='ORCL')
        conn = cx_Oracle.connect(user='rm96960', password='180201', dsn=dsn)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM TB_ALUNO')
        rows = cursor.fetchall()
        for row in rows:
            print(row)
            print(f'Id: {row[0]}')
            print(f'Nome: {row[1]}')
        cursor.close()
        conn.close()
    
    else:
        dsn = cx_Oracle.makedsn(host='oracle.fiap.com.br', port=1521, sid='ORCL')
        conn = cx_Oracle.connect(user='rm96960', password='180201', dsn=dsn)
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