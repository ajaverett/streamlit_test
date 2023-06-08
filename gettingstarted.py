# Import necessary libraries
import streamlit as st
#https://docs.streamlit.io/library/api-reference/widgets/st.button

# Title
st.title('This is the title')

# Typing text
user_text = st.text_area("Enter Some text here")
st.write(f"You just typed: {user_text}")


# Button
if st.checkbox("Show/Hide"):
    st.write("You just clicked me")


# Radio button
status = st.radio("Do you like green or yellow", ("Green!", "Yellow!", "Red!"))
if status == "Green!":
    st.success("this is a success message")
elif status == "Yellow!":
    st.warning("this is a warning message")
elif status == "Red!":
    st.error("this is an error message")



# Select box
occupation = st.selectbox("Your occupation", ["Programmer", "Data Scientist", "Doctor", "Businessman"])
st.write(f"You selected {occupation}")

