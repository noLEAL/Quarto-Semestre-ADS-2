import mysql.connector


def consultar_produto_id(produto_id):
    # Conectando ao banco de dados MySQL
    conexao = mysql.connector.connect(
        host="localhost",  # Substitua pelo endereço do servidor MySQL, se necessário
        user="admin",  # Substitua pelo seu nome de usuário do MySQL
        password="admin",  # Substitua pela sua senha do MySQL
        database="dbmercado"  # Substitua pelo nome do banco de dados
    )

    try:
        cursor = conexao.cursor()

        # Consultando um produto pelo id
        consulta = "SELECT * FROM produtos WHERE id = %s"
        valores = (produto_id,)
        cursor.execute(consulta, valores)

        # Buscando o resultado da consulta
        produto = cursor.fetchone()

        # Exibindo o produto consultado
        if produto:
            print(f"Produto encontrado: {produto}")
        else:
            print("Produto não encontrado.")

    except mysql.connector.Error as err:
        print(f"Erro ao acessar o banco de dados: {err}")

    finally:
        # Fechar a conexão
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()
