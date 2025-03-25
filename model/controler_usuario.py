from data.conexao import Conexao

class Usuario: 

    def cadastrar_usuario (login, nome, senha):

        # cadastrando as informações no banco de dados
        conexao = Conexao.criar_conexao()
        
        #o cursor sera responsavel por manipular o banco de dados
        cursor = conexao.cursor()

        #criando o SQL q sera executado
        sql = """insert into tb_usuarios
                    (login, nome, senha)
                    VALUES
                    (%s, %s, %s)
                    
                    """
        valores = (login, nome, senha)

        # executando o comando sql
        cursor.execute(sql, valores)

        #confirma a alteração
        conexao.commit()

        #fecho a conexao com o banco
        cursor.close()
        conexao.close()