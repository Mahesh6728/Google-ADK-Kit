from google import genai
import os
#genai.configure(api_key=os.getenv("AIzaSyAxKwaRA9FtK-7j-DkEql0CL41tb44hrPs"))  #
#client = genai.Client(api_key= "AIzaSyAxKwaRA9FtK-7j-DkEql0CL41tb44hrPs") # Set your API key here or use environment variable
MODEL = "gemini-3-flash-preview" # Specify the model to use
client = genai.Client(api_key ="AIzaSyAxKwaRA9FtK-7j-DkEql0CL41tb44hrPs")
