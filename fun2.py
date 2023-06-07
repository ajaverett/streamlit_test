# Import necessary libraries
import streamlit as st
import spacy
from spacy import displacy

nlp = spacy.load('en_core_web_sm')
st.title('Streamlit Named Entity Recognition')
st.sidebar.header('Enter Text Here')
user_text = st.sidebar.text_area("")

# Named Entity Recognition
doc = nlp(user_text)
entities = [(ent.text, ent.label_) for ent in doc.ents]

# Display entities
st.write("Entities: ", entities)

# Visualize named entities
html = displacy.render(doc, style="ent")
st.write(html, unsafe_allow_html=True)
