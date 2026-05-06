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
 
 st.subheader("Aplicación 1")
 image = Image.open('pocoyoynina.jpg')
 st.image(image, width=220)
 st.write("Introducción: Mi Primera Aplicación"
) 
 url = "https://introduccionmanuela.streamlit.app/"
 st.write(f"App 1: [Enlace]({url})")

  
 st.subheader("Aplicación 4")
 image = Image.open('reconocimiento.png')
 st.image(image, width=220)
 st.write("Reconocimiento Óptico de caracteres"
) 
 url = "https://imagentexto.streamlit.app/"
 st.write(f"App 4: [Enlace]({url})")

with col2:
 st.subheader("Aplicación 2")
 image = Image.open('ricitos.jpg')
 st.image(image, width=110)
 st.write("Texto a audio: Cuento Ricitos de Oro") 
 url = "https://immmanuela.streamlit.app/"
 st.write(f"App 2: [Enlace]({url})")

  
 st.subheader("Aplicación 5")
 image = Image.open('ricitos.jpg')
 st.image(image, width=110)
 st.write("Cmbinación") 
 url = "https://ocr-audio-manuela.streamlit.app/"
 st.write(f"App 2: [Enlace]({url})")

with col3:
 st.subheader("Aplicación 3")
 image = Image.open('traductor.jpg')
 st.image(image, width=140)
 st.write("Traductor") 
 url = "https://traductormanuela.streamlit.app/"
 st.write(f"App 3: [Enlace]({url})")




