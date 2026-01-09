from datetime import datetime #in case of multiple tool.
def search(query): # A simple search tool, 1st tool.
    if "weather" in query.lower():
        return "The current weather is sunny with a temperature of 75°F."
