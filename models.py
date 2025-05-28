import os
import google.generativeai as genai
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

# Configurar la clave API de Gemini
# genai.configure() buscará GOOGLE_API_KEY en las variables de entorno
try:
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY no está configurada en las variables de entorno.")
    genai.configure(api_key=api_key)
    print("API de Gemini configurada.")
except ValueError as e:
    print(f"Error de configuración de la API: {e}")
    print("Asegúrate de que tu GOOGLE_API_KEY esté correctamente establecida en tu archivo .env.")
    exit()


print("\nModelos disponibles de Google Gemini:")
for m in genai.list_models():
    # Solo mostrar los modelos que soportan el método 'generateContent'
    # que es el que se usa para chat/texto.
    if 'generateContent' in m.supported_generation_methods:
        print(f"- {m.name} (Supported methods: {m.supported_generation_methods})")
    # Para ver TODOS los modelos, comenta la línea de arriba y descomenta esta:
    # print(f"- {m.name} (Supported methods: {m.supported_generation_methods}) (Input Token Limit: {m.input_token_limit})")