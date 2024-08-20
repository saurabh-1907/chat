# gemini_api.py
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class GeminiAPI:
    def __init__(self):
        # Configure the API key from environment variable
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable not set")
        genai.configure(api_key=api_key)
        # Initialize the model
        self.model = genai.GenerativeModel('gemini-1.5-flash')

    def generate_response(self, prompt):
        response = self.model.generate_content(prompt)
        # Check the response object and handle it appropriately
        if hasattr(response, 'text'):
            return response.text
        else:
            raise ValueError("Response object does not have 'text' attribute")
