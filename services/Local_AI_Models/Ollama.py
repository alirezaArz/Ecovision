import ollama
import json
import os
def answer(data):

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DATA_PATH = os.path.join(BASE_DIR, "model.json")

    with open(mode="r", file=DATA_PATH) as file:
        odel = json.load(file)["model"]

    try:
        response = ollama.chat(model=odel, messages=[{

            'role': 'user', 
            
            'content': f"analyze this{data}",
            "category": "news",
            "importance": "medium",
            "date": "2025-07-05T02:15:08.852514"
        }
            ])
        response = response.message.content
        return(response)
    except Exception as e:
        print(f"couldn't get accessed to the local-ai, check ollama and try again: {e}")


