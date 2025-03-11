import mysql.connector

class Conexao:
    
    def criar_conexao():
        #  criando a conexao
        conexao = mysql.connector.connect(host = "localhost", 
                                        port = 3306,
                                        user = "root",
                                        password = "root",
                                        database = "db_comentarios")
        
        return conexao