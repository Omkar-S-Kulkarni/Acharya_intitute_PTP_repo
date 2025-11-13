import requests
import json

OLLAMA_BASE_URL = "http://127.0.0.1:11434"

def ask_model(model_name, prompt):
    """
    Query Ollama model and return plain English text.
    Handles streaming line-delimited JSON responses.
    """
    if not model_name:
        model_name = "phi3:mini"

    url = f"{OLLAMA_BASE_URL}/api/chat"
    payload = {
        "model": model_name,
        "messages": [{"role": "user", "content": prompt}]
    }
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(url, json=payload, headers=headers, stream=True)
        full_text = ""

        # Read line-delimited JSON
        for line in response.iter_lines():
            if not line:
                continue
            try:
                obj = json.loads(line)
                content = obj.get("message", {}).get("content")
                if content:
                    full_text += content
            except json.JSONDecodeError:
                # Skip invalid lines
                continue

        # Clean up extra spaces or newlines
        return full_text.replace("\n\n", "\n").strip()

    except Exception as e:
        return f"Error contacting model: {str(e)}"


def summarize_text(text, model_name="phi3:mini"):
    prompt = f"Summarize this document concisely:\n{text}"
    return ask_model(model_name, prompt)


def extract_insights(text, model_name="phi3:mini"):
    prompt = f"Extract key insights and recommendations in readable English:\n{text}"
    return ask_model(model_name, prompt)
