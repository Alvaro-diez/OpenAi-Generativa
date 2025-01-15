import streamlit as st
from openai import AzureOpenAI
import os
from dotenv import load_dotenv
load_dotenv()

client = AzureOpenAI(
  azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
  api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
  api_version="2024-02-15-preview"
)
model='gpt-4o-mini'


## Lanzar programa con `streamlit run email_app.py`

def limpiar():
    st.rerun()

def generar_resumen(email):
    response = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "Eres un asistente para resumir emails. Las respuestas que des tienen que ser en español independientemente del idioma del email"},
            {"role": "user", "content": f"Haz un resumen del siguiente email: {email}"}
        ],
        model=model
    )
    
    return response.choices[0].message.content


def generar_respuesta(email):
    response = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "Eres un asistente para responder emails. Las respuestas que des tienen que ser en español independientemente del idioma del email"},
            {"role": "user", "content": f"Responde al siguiente email: {email}"}
        ],
        model=model
    )
    
    return response.choices[0].message.content


st.title("App de emails")

txtleft, btndrch = st.columns(2)
txtleft.text("Escribe tu email debajo y después presiona un botón.")
if btndrch.button(label="", icon=":material/restart_alt:", use_container_width=False):
    limpiar()


email = st.text_area("Email", placeholder="Contenido del email", height=400)

left, right = st.columns(2)
if left.button("Generate Summary", use_container_width=True):
    st.text(generar_resumen(email))
if right.button("Generate Answer", use_container_width=True):
    st.text(generar_respuesta(email))


