import mysql.connector
from mysql.connector import Error

# Inserir registros em um Banco de Dados MySQL #
try:
    con = mysql.connector.connect(
        host='localhost',
        database='python',
        user='root',
        password='root')
    inserir_produtos = """INSERT INTO produtos
                          (idproduto, nomeproduto, preco, quantidade)
                          VALUES
                          (1, 'Câmera', 850.00, 5),
                          (2, 'Monitor', 1000.00, 7),
                          (3, 'Relógio', 575.00, 10)"""
    cursor = con.cursor()
    cursor.execute(inserir_produtos)
    con.commit()
    print(f'{cursor.rowcount} Registros inseridos na tabela!')
except Error as erro:
    print(f'Falha ao inserir dados no Banco de Dados python: {erro}')
finally:
    if con.is_connected():
        cursor.close()
        con.close()
        print('Conexão ao MySQL finalizada com Sucesso!')








