import os
from dotenv import load_dotenv
from langchain_community.utilities import SQLDatabase # Necesitarás esta importación

load_dotenv()

db_uri = (
    f"postgresql+psycopg2://{os.getenv('POSTGRES_USER')}:"
    f"{os.getenv('POSTGRES_PASSWORD')}@{os.getenv('POSTGRES_HOST')}:"
    f"{os.getenv('POSTGRES_PORT')}/{os.getenv('POSTGRES_DB')}"
)

try:
    db = SQLDatabase.from_uri(db_uri)
    print("Conexión de prueba a la base de datos exitosa.")

    # Intentar listar las tablas directamente
    tables = db.get_table_names()
    print("Tablas encontradas:", tables)

    # También puedes intentar describir una tabla para ver si funciona
 
except Exception as e:
    print(f"Error durante la prueba de conexión o listado de tablas: {e}")
    print("VERIFICA tus credenciales en .env y que PostgreSQL esté corriendo y sea accesible.")