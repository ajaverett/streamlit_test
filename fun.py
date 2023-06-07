# Import necessary libraries
import streamlit as st
from textblob import TextBlob
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity



st.title('Streamlit Sentiment Analysis')

user_text = st.text_area("Enter Semtiment Text Here")

# Sentiment Analysis
blob = TextBlob(user_text)
result = blob.sentiment

# Display Results
st.write("Sentiment polarity: ", round(result.polarity, 3))
st.write("Sentiment subjectivity: ", round(result.subjectivity, 3))

st.markdown("\n\n\n\n")
st.markdown("***")
st.markdown("\n\n\n\n")

st.title('Streamlit Cosine Similarity Analysis')

a1, a2 = st.columns(2)

with a1:
    user_text1 = st.text_area("Text 1")

with a2:
    user_text2 = st.text_area("Text 2")


# Calculate and display cosine similarity
if user_text1 != "" and user_text2 != "":
    try:
        # Create vectors for each text
        vectorizer = TfidfVectorizer().fit_transform([user_text1, user_text2])
        st.write("Cosine similarity: ", round(cosine_similarity(vectorizer)[0,1], 2))
    except Exception as e:
        st.write("Error: ", str(e))
else:
    st.write("Please enter two texts to compare")