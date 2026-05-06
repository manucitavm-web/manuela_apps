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
 image = Image.open('reconocimiento1.png')
 st.image(image, width=200)
 st.write("Reconocimiento Óptico de caracteres, Camara"
) 
 url = "https://imagentexto.streamlit.app/"
 st.write(f"App 4: [Enlace]({url})")

  
 st.subheader("Aplicación 7")
 image = Image.open('em.png')
 st.image(image, width=200)
 st.write("Análisis de Sentimiento"
) 
 url = "https://sentimentamanu.streamlit.app/"
 st.write(f"App 7: [Enlace]({url})")

  
 st.subheader("Aplicación 10")
 image = Image.open('detec.png')
 st.image(image, width=500)
 st.write("Yolo, Detección de Objetos en Imágenes"
) 
 url = "https://yolov5manuela.streamlit.app/"
 st.write(f"App 10: [Enlace]({url})")


with col2:
 st.subheader("Aplicación 2")
 image = Image.open('ricitos.jpg')
 st.image(image, width=110)
 st.write("Texto a audio: Cuento Ricitos de Oro") 
 url = "https://immmanuela.streamlit.app/"
 st.write(f"App 2: [Enlace]({url})")

  
 st.subheader("Aplicación 5")
 image = Image.open('reconocimiento2.png')
 st.image(image, width=190)
 st.write("Reconocimiento Óptico de caracteres, Imagen") 
 url = "https://ocr-audio-manuela.streamlit.app/"
 st.write(f"App 5: [Enlace]({url})")


 st.subheader("Aplicación 8")
 image = Image.open('pyr.png')
 st.image(image, width=500)
 st.write("Demo de TF-IDF con Preguntas y Respuestas, Inglés") 
 url = "https://demomanuelaingles.streamlit.app/"
 st.write(f"App 8: [Enlace]({url})")


 st.subheader("Aplicación 11")
 image = Image.open('reco.png')
 st.image(image, width=500)
 st.write("Detección de gestos en aplicación TM") 
 url = "https://tmmanuela.streamlit.app/"
 st.write(f"App 11: [Enlace]({url})")

with col3:
 st.subheader("Aplicación 3")
 image = Image.open('traductor.jpg')
 st.image(image, width=150)
 st.write("Traductor Audio - Texto") 
 url = "https://traductormanuela.streamlit.app/"
 st.write(f"App 3: [Enlace]({url})")

  
 st.subheader("Aplicación 6")
 image = Image.open('maquillaje2.png')
 st.image(image, width=150)
 st.write("Nube de palabras") 
 url = "https://wordcloudmanu.streamlit.app/"
 st.write(f"App 6: [Enlace]({url})")


 st.subheader("Aplicación 9")
 image = Image.open('pyr2.png')
 st.image(image, width=500)
 st.write("Demo de TF-IDF con Preguntas y Respuestas, Español") 
 url = "https://demomanuelaesp.streamlit.app/"
 st.write(f"App 9: [Enlace]({url})")


 st.subheader("Aplicación 12")
 image = Image.open('niños.jpg')
 st.image(image, width=1000)
 st.write("Chat adjunto pdf") 
 url = "https://chatpdfmanuela.streamlit.app/"
 st.write(f"App 12: [Enlace]({url})")



