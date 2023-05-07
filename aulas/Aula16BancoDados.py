#INCLUSÂO
import cx_Oracle
# Cria String de conexão com informações do Host, Porta e SID
dsn = cx_Oracle.makedsn(host='oracle.fiap.com.br', port=1521, sid='ORCL')
# Estabelece conexão com o BD
conn = cx_Oracle.connect(user='rm97324', password='fiap23', dsn=dsn)
# Abrir um cursor para executar comandos SQL
cursor = conn.cursor()
# Inserindo valores na tabela
cursor.execute("INSERT INTO TB_USUARIO (ID, NOME) VALUES (:valor1, :valor2)", valor1=66, valor2='Joseffe')
conn.commit()
print('Registro incluído com sucesso!')
# Fechar o cursor e a conexão com o banco de dados
cursor.close()
conn.close()

#ALTERAÇÃO
import cx_Oracle
# Cria String de conexão com informações do Host, Porta e SID
dsn = cx_Oracle.makedsn(host='oracle.fiap.com.br', port=1521, sid='ORCL')
# Estabelece conexão com o BD
conn = cx_Oracle.connect(user='rm97324', password='fiap23', dsn=dsn)
# Abrir um cursor para executar comandos SQL
cursor = conn.cursor()
# Atualizando valores na tabela
cursor.execute("UPDATE TB_USUARIO SET NOME=:valor1 WHERE ID=:valor2", valor1='Natan', valor2=1)
conn.commit()
print('Registro alterado com sucesso!')
# Fechar o cursor e a conexão com o banco de dados
cursor.close()
conn.close()

#EXCLUSÃO
import cx_Oracle
# Cria String de conexão com informações do Host, Porta e SID
dsn = cx_Oracle.makedsn(host='oracle.fiap.com.br', port=1521, sid='ORCL')
# Estabelece conexão com o BD
conn = cx_Oracle.connect(user='rm97324', password='fiap23', dsn=dsn)
# Abrir um cursor para executar comandos SQL
cursor = conn.cursor()
# Excluindo valores da tabela
cursor.execute("DELETE FROM TB_USUARIO WHERE coluna1=:valor1", valor1=1)
conn.commit()
print('Registro excluído com sucesso!')
# Fechar o cursor e a conexão com o banco de dados
cursor.close()
conn.close()

#SELECT
import cx_Oracle
# Cria String de conexão com informações do Host, Porta e SID
dsn = cx_Oracle.makedsn(host='oracle.fiap.com.br', port=1521, sid='ORCL')
# Estabelece conexão com o BD
conn = cx_Oracle.connect(user='rm97324', password='fiap23', dsn=dsn)
# Abrir um cursor para executar comandos SQL
cursor = conn.cursor()
# Executar uma consulta para ler o conteúdo de uma tabela
cursor.execute('SELECT * FROM TB_USUARIO')
# Buscar todos os resultados da consulta
rows = cursor.fetchall()
# Exibir os resultados
for row in rows:
    print(row)
    print(f'Id: {row[0]}')
    print(f'Nome: {row[1]}')
# Fechar o cursor e a conexão com o banco de dados
cursor.close()
conn.close()