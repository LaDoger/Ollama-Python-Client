import json
import requests


# Set system prompt here
system_prompt = """Be concise!"""

# Set user prompt here
user_prompt = """Teach me yoga.
"""


url = 'http://localhost:11434/api/generate'
data = {
    "model": "mistral",
    "system": system_prompt,
    "prompt": user_prompt,
    "stream": False
}

response = requests.post(url, json=data)
response_data = json.loads(response.text)

print(response_data["response"])