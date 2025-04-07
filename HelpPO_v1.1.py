import streamlit as st
from anthropic import Anthropic

# Configuración de la página
st.set_page_config(page_title="App con Claude", page_icon="🤖")

# Inicializar el cliente de Anthropic
@st.cache_resource
def get_client():
    return Anthropic(api_key=st.secrets["ANTHROPIC_API_KEY"])

client = get_client()

# Interfaz de usuario
st.title("Conversación con Claude")

# Inicializar historial de chat en la sesión
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar mensajes anteriores
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Campo de entrada para el usuario
user_input = st.chat_input("Escribe tu mensaje aquí...")

if user_input:
    # Añadir mensaje del usuario al historial
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Mostrar mensaje del usuario
    with st.chat_message("user"):
        st.markdown(user_input)
    
    # Generar respuesta con Claude
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        response = client.messages.create(
            model="claude-3-7-sonnet-20250219",
            max_tokens=1000,
            messages=[
                {"role": m["role"], "content": m["content"]} 
                for m in st.session_state.messages
            ]
        )
        
        assistant_response = response.content[0].text
        message_placeholder.markdown(assistant_response)
    
    # Añadir respuesta de Claude al historial
    st.session_state.messages.append({"role": "assistant", "content": assistant_response})