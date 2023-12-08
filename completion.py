import requests

url = 'http://localhost:11434/api/generate'
data = {
    "model": "mistral",
    "system": "You always reply only with the word 'doge', and nothing else.",
    "prompt": "haha"
}

response = requests.post(url, json=data)

print(response.text)