import ollama
import asyncio
import json
import os

def load_host_url_from_config():
    """Reads the configuration from gmkey.json and returns the host URL."""
    try:
        # Create the full path to the config file
        config_path = os.path.join(os.path.dirname(__file__), 'gmkey.json')
        with open(config_path, 'r', encoding='utf-8') as f:
            config = json.load(f)
        
        # Prioritize static domain, otherwise use random URL
        host_url = config.get("MY_STATIC_DOMAIN") or config.get("NGROK_RANDOM_URL")
        return host_url
        
    except (FileNotFoundError, json.JSONDecodeError):
        # Return None if the file doesn't exist or is invalid
        return None

async def get_ai_response(prompt: str) -> str:
    """
    Sends a prompt to the Ollama server and returns the AI's response as a string.
    """
    host_url = load_host_url_from_config()

    if not host_url:
        return "ERROR: Host URL not found or config file is invalid."

    messages = [
        {'role': 'user', 'content': prompt}
    ]

    try:
        client = ollama.AsyncClient(host=host_url)
        response = await client.chat(model='llama3:8b', messages=messages)
        # Directly return the content of the AI's message
        return response['message']['content']
    
    except Exception as e:
        return f"ERROR: An error occurred: {e}"

async def main():
    """Main function to test the response."""
    user_prompt = "what is 3 + 50"
    
    print(f"User > {user_prompt}")
    
    ai_response_text = await get_ai_response(user_prompt)
    
    print(f"AI > {ai_response_text}")
