CREATE DATABASE db_comentarios;
USE db_comentarios;


CREATE TABLE tb_comentario(
	
    usuario varchar (150) not null,
    comentario text not null, 
    cod_comentario int auto_increment primary key,
    data_comentario datetime not null 
    
);

