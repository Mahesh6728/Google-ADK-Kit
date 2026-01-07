from google import genai
import os
from dotenv import load_dotenv
load_dotenv() 
api_key = os.getenv("Mahi_API_KEY")
#client = genai.Client(api_key=api_key)
#genai.configure(api_key=api_key)
#client = genai.Client(api_key=api_key") # Set your API key here or use environment variable
MODEL = "gemini-3-flash-preview" # Specify the model to use
client = genai.Client(api_key = api_key) # Create a client instance

print(api_key)