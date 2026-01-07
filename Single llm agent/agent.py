from google import genai
from tools import search #importing the tool
from config import MODEL#importing model config

System_prompt = """ 
You are an agent. If the user query is related to weather, use the search tool to provide accurate information.
"""

class SingleLLMAgent:
    def __init__(self,client):
        self.client = client
        #self.memory = []  #initialize memory to store conversation history
    def run(self, user_query: str)-> str: #main method to process user query
        if "weather" in user_query.lower():  #reasoning step to decide tool usage
            a = search(user_query)
            #self.memory.append((user_query, a))  #storing in memory
            return a #using the tool
       # conversation_history = "\n".join(self.memory)  #preparing conversation history
       # response = self.client.models.generate_content(contents=f"{System_prompt}\nUser:{user_query}\n{conversation_history}", model = MODEL) #LLM response generation
        response = self.client.models.generate_content(contents=f"{System_prompt}\nUser:{user_query}", model = MODEL) #if no keyword is present then direct LLM response
        a = response.text
        #self.memory.append((user_query, a))  #storing in memory
        
        return a
        