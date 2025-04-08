from hashlib import sha256
from data.conexao import Conexao
from flask import session

class Usuario: 

    def cadastrar_usuario (login, senha, nome):

        # criptografando a senha
        senha = sha256(senha.encode()).hexdigest()

        # cadastrando as informações no banco de dados
        conexao = Conexao.criar_conexao()
        
        #o cursor sera responsavel por manipular o banco de dados
        cursor = conexao.cursor(dictionary = True)

        #criando o SQL q sera executado
        sql = """insert tb_usuarios
                    (login, senha, nome)
                    VALUES
                    (%s, %s, %s)
                    
                    """
        valores = (login, senha, nome)

        # executando o comando sql
        cursor.execute(sql, valores)

        #confirma a alteração
        conexao.commit()

        #fecho a conexao com o banco
        cursor.close()
        conexao.close()

    def logar (login, senha):

        senha = sha256(senha.encode()).hexdigest()
        
        conexao = Conexao.criar_conexao()
        
        #o cursor sera responsavel por manipular o banco de dados
        cursor = conexao.cursor(dictionary = True)

        #criando o SQL q sera executado
        sql = """SELECT login, nome FROM tb_usuarios WHERE login= %s and binary senha= %s;
                    
                    """
        valores = (login, senha)

        # executando o comando sql
        cursor.execute(sql, valores)

                         # trazer uma linha, uma lista
        resultado = cursor.fetchone()

          #confirma a alteração
        conexao.commit()

        #fecho a conexao com o banco
        cursor.close()
        conexao.close()
        

        if resultado:
            
            session['usuario'] = resultado ['login']
            session['nome_usuario'] = resultado ['nome']
            
            return True
        
        else:

            return False
        

    def logoff():

        session.clear()

      
        