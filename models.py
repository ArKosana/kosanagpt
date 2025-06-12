import os
import requests

def query_model(prompt, model_name):
    token = os.getenv("HUGGINGFACE_TOKEN")
    if not token:
        return "Error: HUGGINGFACE_TOKEN not set."

    API_URL = f"https://api-inference.huggingface.co/models/{model_name}"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    payload = {
        "inputs": prompt,
        "parameters": {"temperature": 0.7, "max_new_tokens": 200},
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()
        result = response.json()

        # Handle Hugging Face response format
        if isinstance(result, list) and "generated_text" in result[0]:
            return result[0]["generated_text"]
        elif isinstance(result, dict) and "error" in result:
            return f"Error: {result['error']}"
        else:
            return str(result)

    except Exception as e:
        return f"Exception: {e}"
