import os
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

from langchain.agents import create_sql_agent
from langchain_community.utilities import SQLDatabase
from langchain_google_genai import ChatGoogleGenerativeAI # ¡Aquí está el cambio!

# 1. Configurar la conexión a PostgreSQL
try:
    db_uri = (
        f"postgresql+psycopg2://{os.getenv('POSTGRES_USER')}:"
        f"{os.getenv('POSTGRES_PASSWORD')}@{os.getenv('POSTGRES_HOST')}:"
        f"{os.getenv('POSTGRES_PORT')}/{os.getenv('POSTGRES_DB')}"
    )
    db = SQLDatabase.from_uri(db_uri)
    print("Conexión a la base de datos PostgreSQL establecida correctamente.")
except Exception as e:
    print(f"Error al conectar a la base de datos: {e}")
    print("Asegúrate de que PostgreSQL esté corriendo y las credenciales en .env sean correctas.")
    exit()

# 2. Inicializar el LLM con Google Gemini
# Asegúrate de que GOOGLE_API_KEY esté configurada en tus variables de entorno.
# Puedes elegir diferentes modelos de Gemini, como "gemini-pro" o "gemini-1.5-flash".
# El "temperature" controla la creatividad; 0.0 es más determinista.
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.0)
print("Modelo Google Gemini inicializado.")


# 3. Crear el Agente SQL
# LangChain es inteligente y, al darle un ChatGoogleGenerativeAI,
# el agente se configurará para usar las herramientas y capacidades de Gemini.
# El tipo de agente "zero-shot-react-description" es común para modelos que no son de OpenAI
# o cuando quieres que el LLM decida las acciones paso a paso.
agent_executor = create_sql_agent(
    llm=llm,
    db=db,
    agent_type="zero-shot-react-description", # Un tipo de agente flexible para Gemini
    verbose=False # Para ver el proceso de razonamiento del agente
)

# 4. Hacer una pregunta al agente
print("\n--- ¡Agente Gemini listo! Haz tu pregunta (escribe 'salir' para terminar) ---")

while True:
    question = input("Tu pregunta: ")
    if question.lower() == 'salir':
        break
    try:
        response = agent_executor.invoke({"input": question})
        print(f"\nRespuesta: {response['output']}")
    except Exception as e:
        print(f"Ocurrió un error al procesar la pregunta: {e}")
        print("Asegúrate de que tu pregunta esté relacionada con la base de datos.")
        print("Verifica el log 'verbose' para más detalles si está activado.")

print("\n--- Sesión terminada ---")