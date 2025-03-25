from flask import Flask, render_template, request, redirect
import datetime
import mysql.connector
from data.conexao import Conexao
from model.controler_mensagem import Mensagem

app = Flask (__name__)

# A partir daqui será as rotas.

@app.route ("/pagina_mensagem")

def pagina_principal():

    #recuperar as mensagens
    comentarios = Mensagem.recuperar_mensagens()

    # enviar os comentarios para o template
    return render_template("paginaPrincipal.html", comentarios = comentarios)

@app.route ("/post/mensagem", methods = ["POST"])

def post_mensagem():

    # peguei as informacoes vindas do html
    usuario = request.form.get("usuario")
    comentario = request.form.get("comentario")
    
    # cadastrando a mensagem usando a Classe mensagem
    Mensagem.cadastrar_mensagem(usuario, comentario)

    # reridiciona para o index
    return redirect ("/pagina_mensagem")


@app.route ("/delete/comentario/<codigo>")

def delete_comentario(codigo):

    Mensagem.deletar_mensagem(codigo)

    return redirect ("/pagina_mensagem")

@app.route("/put/mensagem/adicionar/curtida/<codigo>")

def adicionar_curtida (codigo):

    Mensagem.curtir_mensagem(codigo)

    return redirect ("/pagina_mensagem")

@app.route("/put/mensagem/adicionar/deslike/<codigo>")

def adicionar_deslike (codigo):

    Mensagem.descurtir_mensagem(codigo)

    return redirect ("/pagina_mensagem")

@app.route ("/")

def pagina_login():
    
    return render_template ("paginaLogin.html")

@app.route ("/pagina_cadastro")

def pagina_cadastro():
    
    return render_template ("paginaCadastro.html")


app.run(debug=True)


