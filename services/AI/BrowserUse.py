import asyncio
import json
from browser_use import Agent
from browser_use.llm import ChatGoogle  #change this to chatollama
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, 'gmkey.json')

def getApiKey():
        with open(DATA_PATH, 'r', encoding='utf-8') as file:
            key = json.load(file)
            return key['key']

async def main():
    my_api_key = getApiKey()   #then comment the shit out of this line
    if not my_api_key:                      #and also these 2 line
        return                                 # //

    agent = Agent(
        task="Compare the price of gpt-4o and DeepSeek-V3",
        llm=ChatGoogle(model="gemini-2.0-flash", api_key=my_api_key),    #change this to chatollama too and remove the api_key   and set your ollama llm versioo.
    )
    await agent.run()

#asyncio.run(main())         then take this out of bein comment
