# Ollama-Python-Client
Python script to access Ollama APIs


## How to
1. To use this script, you need to install [Ollama](https://ollama.ai/):
```bash
curl https://ollama.ai/install.sh | sh
```

2. Then you need to download a model in Ollama (using [mistral](https://ollama.ai/library/mistral) as an example):
```bash
ollama run mistral
```

3. Then you execute `completion.py` or `chat.py`:
```bash
python3 completion.py
```
```bash
python3 chat.py
```