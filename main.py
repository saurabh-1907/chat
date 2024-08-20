# main.py
import streamlit as st
from gemini_api import GeminiAPI

# Pass the API key directly if not set as an environment variable
api_key = "AIzaSyDwjOTVmkqKtBoKYXG7SIjE0yJnxdKshto"  # Replace with your actual API key
gemini_api = GeminiAPI(api_key)

def main():
    st.title("Chatbot with Gemini API")
    
    user_input = st.text_input("You:", "")
    
    if st.button("Send"):
        if user_input:
            response = gemini_api.generate_response(user_input)
            st.text_area("Chatbot:", response, height=150)
        else:
            st.warning("Please enter a message!")

if __name__ == "__main__":
    main()
