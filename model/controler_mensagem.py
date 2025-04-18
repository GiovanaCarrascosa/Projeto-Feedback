import datetime

from data.conexao import Conexao

class Mensagem: 

    def cadastrar_mensagem (nome, comentario, curtidas = 0):

        data_hora = datetime.datetime.today()

        # cadastrando as informações no banco de dados
        conexao = Conexao.criar_conexao()
        
        #o cursor sera responsavel por manipular o banco de dados
        cursor = conexao.cursor()

        #criando o SQL q sera executado
        sql = """insert into tb_comentarios
                    (nome, comentario, data_hora, curtidas)
                    VALUES
                    (%s, %s, %s, %s)
                    
                    """
        valores = (nome, comentario, data_hora, curtidas)

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

        sql = """select cod_comentario, nome, comentario, data_hora, curtidas from tb_comentarios;"""

        #executando o comando sql
        cursor.execute(sql)

        # recuperando os dados e guardando em uma variavel
        resultado = cursor.fetchall()

        #fecho a conexao com o banco
        cursor.close()
        conexao.close()
        
        return resultado
    
    def deletar_mensagem (codigo):

            #criar conexao
            conexao = Conexao.criar_conexao()

            cursor = conexao.cursor(dictionary = True)

                                                                    # isso vai ser substituido por outra coisa
            sql = """DELETE FROM tb_comentarios WHERE cod_comentario = %s;"""

            valores = (codigo,)

            #executando o comando sql
            cursor.execute(sql, valores)

            conexao.commit()

            #fecho a conexao com o banco
            cursor.close()
            conexao.close()

    def curtir_mensagem (codigo):

            #criar conexao
            conexao = Conexao.criar_conexao()

            cursor = conexao.cursor(dictionary = True)

                                                                    # isso vai ser substituido por outra coisa
            sql = """update tb_comentarios SET curtidas = curtidas + 1 WHERE cod_comentario = %s;"""

            valores = (codigo,)

            #executando o comando sql
            cursor.execute(sql, valores)

            conexao.commit()

            #fecho a conexao com o banco
            cursor.close()
            conexao.close()

    def descurtir_mensagem (codigo):

            #criar conexao
            conexao = Conexao.criar_conexao()

            cursor = conexao.cursor(dictionary = True)

                                                                    # isso vai ser substituido por outra coisa
            sql = """update tb_comentarios SET curtidas = curtidas - 1 WHERE cod_comentario = %s;"""

            valores = (codigo,)

            #executando o comando sql
            cursor.execute(sql, valores)

            conexao.commit()

            #fecho a conexao com o banco
            cursor.close()
            conexao.close()

    def ultima_mensagem (nome, comentario):
          
            #criar conexao
            conexao = Conexao.criar_conexao()

            cursor = conexao.cursor(dictionary = True)
                                                    
            sql = """SELECT nome, comentario FROM tb_usuarios WHERE nome = %s and comentario = %s;"""

            valores = (nome, comentario,)

            #executando o comando sql
            cursor.execute(sql, valores)

            ultimo_comentario = cursor.getone()

            conexao.commit()

            #fecho a conexao com o banco
            cursor.close()
            conexao.close()

                
        
