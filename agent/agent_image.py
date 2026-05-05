from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from langchain.messages import HumanMessage, AIMessage
from langchain.tools import tool
from langgraph.checkpoint.memory import InMemorySaver
from tools.busqueda_web_recetas import busqueda_web_recetas
from tools.busqueda_precios_ingredientes import busqueda_precios_ingredientes
from ipywidgets import FileUpload
from IPython.display import display
import base64
from pprint import pprint 
from IPython.display import display

load_dotenv()

# ---

modelo = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash",
    temperature = 0.8 
 )

# ---
system_prompt = f"""
Eres un cheff profesional que ayuda a personas que no son expertos en cocinar, a crear recetas de comidas. 
Explicas con mucha claridad 

Cadena de pensamiento:
1- Si el usuario no te pasó los ingredientes que tiene, debes invitarlo a que te diga que ingredientes tiene
Ejemplo de salida:
Mar2Cheff: Hola! Soy Mar2! Tu cheff virtual. Por favor, indicame que ingredientes tenes

2- Si el usuario te indica que ingredientes tiene, debes procesarlos para poder recomendale una receta e indicarle la misma
Para buscar enlaces de recetas, usa la herramienta llamada  busqueda_web_recetas
Ejemplo de salida:
Mar2Cheff: Tienes los siguientes ingredientes:

- Arroz
- Pechuga de Pollo
Con estos ingredientes puesdes hacer Arroz con pollo.

Puedes ver recetas recomendadas en: 
* enlace1
* enlace2
* enlace3

Si puedes, puedes sumar estos ingredientes que complementan la receta:
- Zanahoria

"""


# --
Mar2cheff_multimodal = create_agent(
    model = modelo,
    tools = [busqueda_web_recetas, busqueda_precios_ingredientes],
    system_prompt= system_prompt,
    checkpointer= InMemorySaver()
)

#---
config = {"configurable": {
    "thread_id": "123abc"
}}

# ---

def call_agent_image(query: str, img_bytes: bytes | None = None):
    # Construir contenido del mensaje según si hay imagen o no
    content = [{"type": "text", "text": query}]
    
    # Agregar imagen solo si está presente
    if img_bytes is not None:
        img_b64 = base64.b64encode(img_bytes).decode("utf-8")
        content.append({
            "type": "image",
            "base64": img_b64,
            "mime_type": "image/jpeg",
        })

    response = Mar2cheff_multimodal.invoke(
        {
            "messages": [
                HumanMessage(content=content)
            ]
        },
        config
    )

    # Debug opcional
    for message in response["messages"]:
        print(f"{message.type}")
        print(message.content, "\n")

        if hasattr(message, "tool_calls"):
            print(message.tool_calls, "\n")

    # Manejo más robusto del output
    last_message = response["messages"][-1]

    if isinstance(last_message.content, list):
        for block in last_message.content:
            if block.get("type") == "text":
                return block.get("text")

    return last_message.content