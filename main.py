# main.py
import streamlit as st
from gemini_api import GeminiAPI

# Initialize the GeminiAPI object
gemini_api = GeminiAPI()

def main():
    st.title("Chatbot")
    
    user_input = st.text_input("You:", "")
    
    if st.button("Send"):
        if user_input:
            response = gemini_api.generate_response(user_input)
            st.text_area("Chatbot:", response, height=150)
        else:
            st.warning("Please enter a message!")

if __name__ == "__main__":
    main()
