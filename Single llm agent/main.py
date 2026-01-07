from agent import SingleLLMAgent#import the agent class
from config import client as config#
agent = SingleLLMAgent(client = config) #create an instance of the agent
while True: #infinite loop to keep the program running
    user_query = input("User: ") #get user input
    if user_query.lower() in ["exit", "quit"]: #exit condition
        print("Exiting the agent. Goodbye!")
        break
    answer = agent.run(user_query) #get the agent's response
    print("Agent:", answer) #print the responses