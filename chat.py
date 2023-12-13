import json
import requests


# Choose the model you want to use. By default it's "mistral"
model = "mistral"

# Set system prompt here
system_prompt = """reply only with the word 'dogecoin'"""

url = 'http://localhost:11434/api/chat'
data = {
    "model": model,
    "messages": [
        {
            
            "role": "system",
            "content": system_prompt
        },
        {

            "role": "user",
            "content": "hi"
        }
    ],
    "stream": False
}

response = requests.post(url, json=data)
response_data = json.loads(response.text)

print(response_data["message"]["content"])