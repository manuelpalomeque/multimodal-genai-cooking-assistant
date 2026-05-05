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
    .main-title {
        font-family: 'Georgia', serif;
        color: #7d4f39;
        text-align: center;
        padding: 1rem;
        border-bottom: 2px solid #e1d4c1;
        margin-bottom: 2rem;
    }

    .stChatMessage {
        background-color: #ebdbc7 !important;
        border: 2px solid #eee;
        border-radius: 15px !important;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.05);
    }
    </style>

    <h1 class="main-title">👩🏻‍🍳 Mar2 BOTtana: Tu Chef Virtual</h1>
""", unsafe_allow_html=True)

# 3. Sidebar
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3448/3448099.png", width=100)
    st.header("Configuraciones")
    st.info("Contame qué tenés y te armo una receta 👀")

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
    "📸 Subí una imagen (opcional)",
    type=["jpg", "jpeg", "png"]
)

# 7. Input del usuario
if query := st.chat_input("Hola! indicame que ingredientes tienes!"):

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