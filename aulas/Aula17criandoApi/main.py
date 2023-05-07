import cx_Oracle
from fastapi import FastAPI, HTTPException, status
from fastapi.responses import JSONResponse
from Usuario import Usuario
app = FastAPI()
dsn = cx_Oracle.makedsn(host='oracle.fiap.com.br', port=1521, sid='ORCL')

@app.post("/incluir_usuario", status_code=status.HTTP_201_CREATED)
def incluir_usuario(usuario: Usuario):
    try:
        conn = cx_Oracle.connect(user='rm97324', password='fiap23', dsn=dsn)
        cursor = conn.cursor()

        cursor.execute("INSERT INTO TB_USUARIO (ID, NOME) VALUES (:valor1, :valor2)", valor1=usuario.id, valor2=usuario.nome)
        conn.commit()

        return {"message": "Usuário incluído com sucesso!"}
    except Exception as e:
        raise HTTPException(status_code=400, detail="Erro ao inserir usuário - " + str(e))
    finally:
        cursor.close()
        conn.close()

@app.put("/atualizar_usuario/{idUsuario}", status_code=status.HTTP_200_OK)
def atualizar_usuario(usuario: Usuario, idUsuario):
    try:
        conn = cx_Oracle.connect(user='rm97324', password='fiap23', dsn=dsn)
        cursor = conn.cursor()

        cursor.execute("UPDATE TB_USUARIO SET NOME=:valor1 WHERE ID=:valor2", valor1=usuario.nome, valor2=idUsuario)
        conn.commit()

        return {"message": "Usuário atualizado com sucesso!"}
    except Exception as e:
        raise HTTPException(status_code=400, detail="Erro ao atualizar o usuário - " + str(e))
    finally:
        cursor.close()
        conn.close()

@app.delete("/excluir_usuario/{idUsuario}", status_code=status.HTTP_200_OK)
def excluir_usuario(idUsuario):
    try:
        conn = cx_Oracle.connect(user='rm97324', password='fiap23', dsn=dsn)
        cursor = conn.cursor()

        cursor.execute("DELETE FROM TB_USUARIO WHERE ID=:valor1", valor1=idUsuario)
        conn.commit()

        return {"message": "Usuário excluído com sucesso!"}
    except Exception as e:
        raise HTTPException(status_code=400, detail="Erro ao excluir o usuário - " + str(e))
    finally:
        cursor.close()
        conn.close()

@app.get("/listar_usuarios", status_code=status.HTTP_200_OK)
def listar_usuarios():
    try:
        conn = cx_Oracle.connect(user='rm97324', password='fiap23', dsn=dsn)
        cursor = conn.cursor()

        cursor.execute('SELECT ID, NOME FROM TB_USUARIO ORDER BY ID')

        rows = cursor.fetchall()

        listaUsuarios = []

        for row in rows:
            usuario = {"id": row[0], "nome": row[1]}
            listaUsuarios.append(usuario)

        return listaUsuarios
    except Exception as e:
        raise HTTPException(status_code=400, detail="Erro ao selecionar os usuários - " + str(e))
    finally:
        cursor.close()
        conn.close()

@app.get("/lista_usuario/{idUsuario}", status_code=status.HTTP_200_OK)
def lista_usuario(idUsuario: int):
    try:
        conn = cx_Oracle.connect(user='rm97324', password='fiap23', dsn=dsn)
        cursor = conn.cursor()

        cursor.execute("SELECT ID, NOME FROM TB_USUARIO WHERE ID=:valor1", valor1=idUsuario)

        rows = cursor.fetchall()

        if (idUsuario > len(rows)):
            return JSONResponse(status_code=400, content={"message": "Usuário não existente!"})
        for row in rows:
            if (row[0] == idUsuario):
                usuario = {"id": row[0], "nome": row[1]}
                break
        return usuario
    except Exception as e:
        raise HTTPException(status_code=400, detail="Erro ao selecionar o usuário - " + str(e))
    finally:
        cursor.close()
        conn.close()