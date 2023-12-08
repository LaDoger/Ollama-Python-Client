# The chat API is not live yet as of 8 Dec 2023. Please be patient.

import requests

url = 'http://localhost:11434/api/chat'
data = {
    "model": "mistral",
    "messages": [
        {
            "role": "user",
            "content": "reply only with the word 'dogecoin'"
        }
    ]
}

response = requests.post(url, json=data)

print(response.text)