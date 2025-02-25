from flask import Flask, render_template, request, redirect
import datetime
import mysql.connector

app = Flask (__name__)

# A partir daqui será as rotas.

@app.route ("/")

def pagina_principal():

    return render_template ("paginaPrincipal.html")



@app.route ("/post/mensagem", methods = ["POST"])

def post_mensagem():

    # peguei as informacoes vindas do html
    usuario = request.form.get("usuario")
    comentario = request.form.get("comentario")
    data_comentario = datetime.datetime.today()

    # cadastrando as informações no banco de dados
    conexao = mysql.connector.connect(host = "localhost", 
                                      port = 3306,
                                      user = "root",
                                      password = "root",
                                      database = "db_comentarios")
    
    #o cursor sera responsavel por manipular o banco de dados
    cursor = conexao.cursor()

    #criando o SQL q sera executado
    sql = """insert into tb_comentario
                (usuario, comentario, data_comentario)
                VALUES
                (%s, %s, %s)
                
                """
    valores = (usuario, comentario, data_comentario)

    # executando o comando sql

    cursor.execute(sql, valores)

    #confirma a alteração

    conexao.commit()

    #fecho a conexao com o banco
    cursor.close()
    conexao.close()

    # reridiciona para o index
    return redirect ("/")


app.run(debug=True)