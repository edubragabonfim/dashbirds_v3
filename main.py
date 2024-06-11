import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv
import os

load_dotenv()

def connect_to_db():
    try:
        # Configurações de conexão
        connection = psycopg2.connect(
            user=os.getenv('PG_USER'),
            password=os.getenv('PG_PWD'),
            host=os.getenv('PG_HOST'),
            port=os.getenv('PG_PORT'),
            database=os.getenv('PG_DATABASE')
        )
        cursor = connection.cursor()

        # Executa a query
        query = sql.SQL("SELECT * FROM public.gpt_users;")
        cursor.execute(query)
        records = cursor.fetchall()

        print("Resultado da query:")
        for row in records:
            print(row)

    except (Exception, psycopg2.Error) as error:
        print("Erro ao conectar ao PostgreSQL", error)
    finally:
        # Fechar a conexão
        if connection:
            cursor.close()
            connection.close()
            print("Conexão ao PostgreSQL fechada")

if __name__ == "__main__":
    connect_to_db()
