import streamlit as st

import sys
from pathlib import Path

# Agregar la raíz del proyecto al path
sys.path.insert(0, str(Path(__file__).parent.parent))

from agent.agent_image import call_agent_image


# 1. Configuración de la página
st.set_page_config(
    page_title="Mar2 BOTtana - Chef Virtual",
    page_icon="👩🏻‍🍳",
    layout="centered"
)

# 2. CSS personalizado
st.markdown("""
    <style>
    @import url('[https://fonts.googleapis.com/css2?family=Caveat:wght@700&display=swap](https://fonts.googleapis.com/css2?family=Caveat:wght@700&display=swap)');
            
    .main-title {
        font-family: 'Caveat', cursive !important;
        color: #f57e45 !important;
        text-align: left;
        padding: 1rem;
        border-bottom: 2px solid #e1d4c1;
        margin-bottom: 2rem;
    }

    /* 1. Estilo base para AMBAS burbujas */
    [data-testid="stChatMessage"] {
        border-radius: 20px !important;
        margin-bottom: 15px;
        padding: 15px;
        border: 2px solid #FFD56B !important;
        background-color: #f5fcd4;
    
    }

    /* Personalización del Sidebar */
    [data-testid="stSidebar"] {
        background-image: url("https://raw.githubusercontent.com/manuelpalomeque/multimodal-genai-cooking-assistant/refs/heads/main/data/FondoLineasColores.jpg")!important; 

    }

    
    /* Estilo para los botones (opcional) */
    .stButton >button {
        border-radius: 20px;
        border: 1px solid #FF6B35;
        color: #FF6B35;
    }
    </style>
            
    <h1 class="main-title">Hola, soy Mar2 BOTtana</h1>
    <h5>Decime qué ingredientes tenés y te genero recetas increíbles </h5>
""", unsafe_allow_html=True)

# 3. Sidebar
with st.sidebar:
    st.image("https://raw.githubusercontent.com/manuelpalomeque/multimodal-genai-cooking-assistant/refs/heads/main/data/Mar2.png", width=600)
    st.header("Tu Chef Virtual con IA")
    st.markdown("Estoy lista para cocinar! Sube una imagen de tus ingredientes o dime qué tienes, y crearé algo delicioso para ti.")
    st.markdown("---")
   
    st.markdown("#### Acciones:")

    if st.button("🧹 Limpiar conversación"):
        st.session_state.messages = []
        st.rerun()

# 4. Session state (chat + imágenes)
if "messages" not in st.session_state:
    st.session_state.messages = []

# 5. Mostrar historial
for msg in st.session_state.messages:
    avatar = "👩🏻‍🍳" if msg["role"] == "assistant" else "👤"

    with st.chat_message(msg["role"], avatar=avatar):
        st.markdown(msg["content"])

        # Mostrar imagen si existe
        if "image" in msg and msg["image"] is not None:
            st.image(msg["image"], caption="Imagen enviada", width="stretch")

# 6. Uploader (fuera del input de chat)
uploaded_file = st.file_uploader(
    "📸 Subí una foto de tus ingredientes! 👇🏻",
    type=["jpg", "jpeg", "png"]
)

# 7. Input del usuario
if query := st.chat_input("Indicame que ingredientes tienes! Ej: Pollo, arroz ..."):

    # Obtener bytes de imagen (forma correcta)
    img_bytes = uploaded_file.getvalue() if uploaded_file else None

    # Guardar mensaje usuario
    st.session_state.messages.append({
        "role": "user",
        "content": query,
        "image": img_bytes
    })

    # Mostrar mensaje usuario
    with st.chat_message("user", avatar="👤"):
        st.markdown(query)

        if img_bytes:
            st.image(img_bytes, caption="Imagen enviada", use_column_width=True)

    # Respuesta del agente
    with st.chat_message("assistant", avatar="👩🏻‍🍳"):
        with st.spinner("Pensando en una receta deliciosa..."):
            try:
                response = call_agent_image(query, img_bytes)

                st.markdown(response)

                # Guardar respuesta
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": response
                })

            except Exception as e:
                st.error(f"¡Ups! Algo salió mal: {e}")