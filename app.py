# importamentos
from flask import Flask, jsonify, render_template, request, redirect
import datetime
import mysql.connector
from data.conexao import Conexao
from model.controler_mensagem import Mensagem
from model.controler_usuario import Usuario
from flask import session

app = Flask (__name__)

app.secret_key = "ArianaGrande"


# A partir daqui será as rotas.
# rota da pagina de comentarios
@app.route ("/pagina_mensagem")

def pagina_principal():

    if "usuario" in session:

        #recuperar as mensagens
        comentarios = Mensagem.recuperar_mensagens()

        # enviar os comentarios para o template
        return render_template("paginaPrincipal.html", comentarios = comentarios)
    
    else:

        return redirect ("/")



# cadastrar mensagem
@app.route ("/post/mensagem", methods = ["POST"])

def post_mensagem():

    # peguei as informacoes vindas do html
    usuario = request.form.get("usuario")
    comentario = request.form.get("comentario")
    
    # cadastrando a mensagem usando a Classe mensagem
    Mensagem.cadastrar_mensagem(usuario, comentario)

    # reridiciona para o index
    return redirect ("/pagina_mensagem")



# deletar mensagem
@app.route ("/delete/comentario/<codigo>")

def delete_comentario(codigo):

    Mensagem.deletar_mensagem(codigo)

    return redirect ("/pagina_mensagem")



# curtir comentario
@app.route("/put/mensagem/adicionar/curtida/<codigo>")

def adicionar_curtida (codigo):

    Mensagem.curtir_mensagem(codigo)

    return redirect ("/pagina_mensagem")



# dar deslike no comentario
@app.route("/put/mensagem/adicionar/deslike/<codigo>")

def adicionar_deslike (codigo):

    Mensagem.descurtir_mensagem(codigo)

    return redirect ("/pagina_mensagem")



# rota pra tela inicial, tela de login
@app.route ("/logoff")

def sair():
    
    Usuario.logoff()

    return render_template ("paginaLogin.html")



@app.route ("/")

def pagina_login():
    
    return render_template ("paginaLogin.html")

@app.route("/post/logar", methods = ["POST"])

def post_logar():

    usuario = request.form.get("login")
    senha = senha = request.form.get("senha")

    esta_logado = Usuario.logar(usuario, senha)

    if esta_logado:

        return redirect ("/pagina_mensagem")
    
    else:

        return redirect ("/")




# rota pra tela de cadastro
@app.route ("/pagina_cadastro")

def pagina_cadastro():
    
    return render_template ("paginaCadastro.html")





@app.route ("/post/usuario", methods = ["POST"])

def post_usuario():

    # peguei as informacoes vindas do html
    login = request.form.get("login")
    senha = request.form.get("senha")
    nome = request.form.get("nome")
   
    # cadastrando o usuario usando a Classe usuario
    Usuario.cadastrar_usuario(login, senha, nome)

    # reridiciona para o index
    return redirect ("/")

@app.route("/api/get/mensagens")

def api_get_mensagens():

    mensagens = Mensagem.recuperar_mensagens()
    return jsonify(mensagens)

@app.route("/api/get/ultimamensagem/<usuario>")

def api_get_ultima_mensagem(usuario):

    mensagem = Mensagem.ultima_mensagem(usuario)
    return jsonify (mensagem)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)


