# 👩🏻‍🍳 Mar2-BOTtana Asistente de cocina multimodal GenAI

Un asistente de cocina inteligente con IA generativa capaz de crear recetas a partir de texto e imágenes.

Desarrollado con una arquitectura de agente modular que utiliza LLM, tools de busqueda de recetas online y consulta de precios de ingredientes en supermercados, junto con una interfaz de chat basada en Streamlit.

---

## 🚀 Demo
El siguiente es un video corto que muestra el funcionamiento del agente:

[Caso de Uso 1](https://github.com/manuelpalomeque/multimodal-genai-cooking-assistant/blob/main/data/Caso_de_uso_1_Input_texto.gif?raw=true)


[Caso de Uso 2](https://github.com/manuelpalomeque/multimodal-genai-cooking-assistant/blob/main/data/Caso_de_uso_2_Input_imagen.gif?raw=true)

Casos de uso:

1.  El usuario introduce los ingredientes que tiene, para solicitar recetas al agente. Este le informa que receta puede hacer con los ingredientes, le devuelve un listado de enlaces a recetas y le sugiere ingredientes faltantes, que podrian complementar la receta.
2. El usuario introduce una imagen de los ingredientes disponibles en su heladera, para que el agente le sugiera recertas en base a sus ingredientes disponibles.
3. El asistente le ofrece consultar los precios d elos ingredientes faltantes en un supermercado, de manera online. Informa los precios de cada ingrediente

---

## ✨ Features

* 🧠 IA conversacional basada en LLM
* 🖼️ Multimodal input (texto + imagen)
* 🍲 Generación de recetas según ingredientes o contexto
* 🔧 Web-augmented responses mediante Tools de búsqueda externas (recetas y precios)
* 🔗 Orquestación de agentes basada en grafos
* 💬 Interfaz de chat interactiva con Streamlit
* 🔐 Configuración basada en el entorno

---

## 🧠 Arquitectura

El sistema sigue un diseño modular y extensible basado en agentes que utiliza la orquestación de grafos:

Input del usuario → Streamlit UI → Agent Core (langchain) → Tools  → LLM → Respuesta

### Componentes:

* **app/** → Interfaz de usuario (Streamlit)
* **agent/** → Lógica de orquestación principal (flujo basado en grafos)
* **tools/** → Funcionalidades externas (búsqueda de recetas, precios, etc.)
* **data/** → Recursos de ejemplo

---

## 🛠️ Tech Stack

* *Core*
    * Python
    * Streamlit
    * dotenv
* *LLM & Orchestration*
    * LangChain
    * LangGraph
    * langchain_google_genai
    * langchain_groq
* *Tools & Integrations*
    * Tavily (web search)
    * requests
* *Data & Processing*
    * markdownify
    * typing
---

## ⚙️ Instalación

```bash
git clone https://github.com/manuelpalomeque/multimodal-genai-cooking-assistant.git
cd multimodal-genai-cooking-assistant
pip install -r requirements.txt
```

---

## 🔐 Variables de Entorno

Crear un archivo `.env`  basado en `.env.example`:

```env
GOOGLE_API_KEY=your_api_key_here 
TAVILY_API_KEY=your_api_key_here
```

---

## ▶️ Ejecutar la app

```bash
streamlit run app/app_images.py
```

---

## 📌 Ejemplo de Uso

**Input:**

> "Hola! tengo pure de tomate y pechuga, que puedo cocinar?"

**Output:**

>"Tienes los siguientes ingredientes:
>
>Puré de tomate
>
>Pechuga de pollo
>
>Con estos ingredientes puedes preparar un delicioso Pollo en salsa de puré de tomate.
>
>Puedes ver recetas recomendadas en:
>
>https://www.recetasnestle.com.mx/recetas/pollo-en-salsa-pure-tomate
>https://cookpad.com/eeuu/buscar/pure%20de%20tomate%20y%20pollo
>https://www.lacostena.com.mx/es/recetas/pechuga-de-pollo-con-sals/
>
>Si puedes, puedes sumar estos ingredientes que complementan la receta:
>
>Cebolla
>
>Ajo
>
>Zanahoria
>
>Papa."

---

## 🧠 Decisiones de diseño

* Separación de responsabilidades entre la interfaz de usuario, la lógica del agente y las herramientas
* Arquitectura modular para facilitar la extensibilidad
* Soporte multimodal como característica principal
* Memoria de corto plazo implementada
* Interfaz limpia y minimalista para una mayor usabilidad

---

## 📈 Futuras mejoras

* Integrar una base de datos vectorial para la recuperación semántica de recetas
* Mejorar la evaluación y el seguimiento
* Implementar en un entorno en la nube
* Añadir análisis nutricional
* Añadir personalización según las preferencias y restricciones dietéticas del usuario.
    * Sin gluten (recetas aptas para celíacos)
    * Recetas aptas para diabéticos
    * Opciones saludables y bajas en calorías

---

## 👨‍💻 Autor

Jonathan Manuel Palomeque – Data Scientist & AI Developer


