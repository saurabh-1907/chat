# gemini_api.py
import google.generativeai as genai

class GeminiAPI:
    def __init__(self, api_key):
        # Configure the API key directly
        genai.configure(api_key=api_key)
        # Initialize the model
        self.model = genai.GenerativeModel('gemini-1.5-flash')

    def generate_response(self, prompt):
        response = self.model.generate_content(prompt)
        return response.text
