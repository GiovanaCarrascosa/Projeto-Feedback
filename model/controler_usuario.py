from hashlib import sha256
from data.conexao import Conexao

class Usuario: 

    def cadastrar_usuario (login, senha, nome):

        # criptografando a senha
        senha = sha256(senha.encode()).hexdigest()

        # cadastrando as informações no banco de dados
        conexao = Conexao.criar_conexao()
        
        #o cursor sera responsavel por manipular o banco de dados
        cursor = conexao.cursor()

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
        cursor = conexao.cursor()

        #criando o SQL q sera executado
        sql = """SELECT login, senha FROM tb_usuarios WHERE login= %s and binary senha= %s;
                    
                    """
        valores = (login, senha)

        # executando o comando sql
        cursor.execute(sql, valores)

        resultado = cursor.fetchone()

        if resultado

        #confirma a alteração
        conexao.commit()

        #fecho a conexao com o banco
        cursor.close()
        conexao.close()
        
        