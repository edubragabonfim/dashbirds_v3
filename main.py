# import psycopg2
# from psycopg2 import sql
# from dotenv import load_dotenv
# import os

# load_dotenv()
# from sqlalchemy import create_engine, text
# from sqlalchemy.orm import sessionmaker

# def connect_to_db():
#     try:
#         # Configurações de conexão
#         db_url = f"postgresql+psycopg2://{os.getenv('PG_USER')}:{os.getenv('PG_PWD')}@{os.getenv('PG_HOST')}:{os.getenv('PG_PORT')}/{os.getenv('PG_DATABASE')}"
#         engine = create_engine(db_url)
#         Session = sessionmaker(bind=engine)
#         session = Session()

#         # Executa a query
#         query = text("SELECT * FROM public.gpt_users;")
#         result = session.execute(query).fetchall()

#         print("Resultado da query:")
#         for row in result:
#             print(row)

#     except Exception as error:
#         print("Erro ao conectar ao PostgreSQL", error)
#     finally:
#         # Fechar a sessão
#         session.close()
#         print("Conexão ao PostgreSQL fechada")

# # Chama a função para testar
# connect_to_db()


# if __name__ == "__main__":
#     connect_to_db()

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)

def run():
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )

    st.write("# Welcome to Streamlit! 👋")

    st.sidebar.success("Select a demo above.")

    st.markdown(
        """
        Streamlit is an open-source app framework built specifically for
        Machine Learning and Data Science projects.
        **👈 Select a demo from the sidebar** to see some examples
        of what Streamlit can do!
        ### Want to learn more?
        - Check out [streamlit.io](https://streamlit.io)
        - Jump into our [documentation](https://docs.streamlit.io)
        - Ask a question in our [community
          forums](https://discuss.streamlit.io)
        ### See more complex demos
        - Use a neural net to [analyze the Udacity Self-driving Car Image
          Dataset](https://github.com/streamlit/demo-self-driving)
        - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
    """
    )


if __name__ == "__main__":
    run()