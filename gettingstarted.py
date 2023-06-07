# Import necessary libraries
import streamlit as st
#https://docs.streamlit.io/library/api-reference/widgets/st.button

st.title('This is the title')



user_text = st.text_area("Enter Some text here")
st.write(f"You just typed: {user_text}")
st.markdown("<br><br><br><br>", unsafe_allow_html=True)



if st.checkbox("Show/Hide"):
    st.write("You just clicked me")
st.markdown("<br><br><br><br>", unsafe_allow_html=True)



status = st.radio("Do you like green or yellow", ("Green!", "Yellow!"))
if status == "Green!":
    st.success("this is a success message")
else:
    st.warning("this is a warning message")
st.markdown("<br><br><br><br>", unsafe_allow_html=True)



# selectbox
occupation = st.selectbox("Your occupation", ["Programmer", "Data Scientist", "Doctor", "Businessman"])
st.write(f"You selected {occupation}")

