import asyncio
import json
from browser_use import Agent
from browser_use.llm import ChatGroq  #change this to chatollama
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, 'gmkey.json')

def getApiKey():
        with open(DATA_PATH, 'r', encoding='utf-8') as file:
            key = json.load(file)
            return key['grog']

async def main():
    my_api_key = getApiKey()   #then comment the shit out of this line
    if not my_api_key:                      #and also these 2 line
        return                                 # //

    agent = Agent(
        task="inside this certain page https://www.nytimes.com/section/business scrap some news (titles and summeries)",
        llm=ChatGroq(model="llama3-70b-8192", api_key=my_api_key),    #change this to chatollama too and remove the api_key   and set your ollama llm versioo.
    )
    await agent.run()

asyncio.run(main())       
