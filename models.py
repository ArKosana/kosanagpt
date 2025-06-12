import os
import requests
from dotenv import load_dotenv

load_dotenv()

HF_TOKEN = os.getenv("HUGGINGFACE_TOKEN")
HEADERS = {"Authorization": f"Bearer {HF_TOKEN}"}

def query_model(prompt, model_name):
    api_url = f"https://api-inference.huggingface.co/models/{model_name}"
    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 256,
            "temperature": 0.7
        }
    }
    response = requests.post(api_url, headers=HEADERS, json=payload)
    if response.status_code != 200:
        return f"Error {response.status_code}: {response.text}"
    try:
        result = response.json()
        # Mistral returns text in list under 'generated_text' key
        if isinstance(result, list) and "generated_text" in result[0]:
            return result[0]['generated_text']
        # fallback for other formats
        return str(result)
    except Exception as e:
        return f"Exception parsing response: {str(e)}"
