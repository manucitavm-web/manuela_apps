import streamlit as st
from PIL import Image
st.title("Mis aplicaciones")

with st.sidebar:
  st.subheader("Creación de Interfaces Multimodales")
  parrafo = (
    "Manuela Vallejo Martínez"
  )
  st.write(parrafo)

url_ia="https://docs.google.com/document/d/1AG81b_IB8lGef8qu-Z6m8dSePfXJrbfv/edit"
st.subheader("En la siguiente enlace podrás encontrar un documento con links y capturas de mis ejercicios prácticos")
st.write(f"Portalio Manuela: [Enlace]({url_ia})")
col1, col2, col3 = st.columns(3)

with col1:
 
 st.subheader("App 1")
 image = Image.open('pocoyoynina.jpg')
 st.image(image, width=200)
 st.write("1.	Introducción: Mi Primera App"
) 
 url = "https://introduccionmanuela.streamlit.app/"
 st.write(f"App 1: [Enlace]({url})")


with col2: 
 st.subheader("App 2")
 image = Image.open('ricitos.jpg')
 st.image(image, width=100)
 st.write("2.	Texto a audio: Cuento Ricitos de Oro") 
 url = "https://immmanuela.streamlit.app/"
 st.write(f"App 2: [Enlace]({url})")

 st.subheader("Análisis de Datos")
 image = Image.open('data_analisis.png')
 st.image(image, width=190)
 st.write("En la siguiente enlace veremos como se pueden analizar datos usando agentes.") 
 url = "https://dataagente.streamlit.app/"
 st.write(f"Datos: [Enlace]({url})")

 st.subheader("Trasnscriptor Audio y Video")
 image = Image.open('OIG3.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos como realizamos transcripciones de audio/video.") 
 url = "https://transcript-whisper.streamlit.app/"
 st.write(f"Transcriptor: [Enlace]({url})")


with col3: 
 st.subheader("Generación en Contexto")
 image = Image.open('Chat_pdf.png')
 st.image(image, width=190)
 st.write("En la siguiente veremos una aplicación que usa RAG a partir de un documento (PDF).") 
 url = "https://chatpdf-cc.streamlit.app/"
 st.write(f"RAG: [Enlace]({url})")

 st.subheader("Análisis de Imagen")
 image = Image.open('OIG4.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos la capacidad de análisis en Imágenes.") 
 url = "https://vision2-gpt4o.streamlit.app/"
 st.write(f"Vision: [Enlace]({url})")
 
 st.subheader("Sistema Ciberfísico")
 image = Image.open('OIG6.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos la capacidad de interacción con el mundo físico.") 
 url = "https://vision2-gpt4o.streamlit.app/"
 st.write(f"Vision: [Enlace]({url})")


