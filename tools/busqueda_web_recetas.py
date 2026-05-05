from langchain.tools import tool
from typing import Dict, Any
from tavily import TavilyClient
from dotenv import load_dotenv

load_dotenv()

tavily_client= TavilyClient()

@tool
def busqueda_web_recetas(query:str) -> Dict[str, Any]:
    """Búsca recetas en la web"""
    return tavily_client.search(query)