import datetime

from data.conexao import Conexao

class Mensagem: 

    def cadastrar_mensagem (usuario, comentario):

        data_comentario = datetime.datetime.today()

        # cadastrando as informações no banco de dados
        conexao = Conexao.criar_conexao
        
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

    def recuperar_mensagens():

        #criar conexao
        conexao = Conexao.criar_conexao()

        cursor = conexao.cursor(dictionary = True)

        sql = """select usuario, comentario, data_comentario from tb_comentario;"""

        #executando o comando sql
        cursor.execute(sql)

        # recuperando os dados e guardando em uma variavel
        resultado = cursor.fetchall()

        #fecho a conexao com o banco
        cursor.close()
        conexao.close()
        
        return resultado
    

