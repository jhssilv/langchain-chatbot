# LangChain Chatbot

## Instalation
```sh
conda install --yes --file requirements.txt
# or
pip install -r requirements.txt
```

## How to use

Create .env and load api keys
```sh
GOOGLE_API_KEY='abc'
OPENAI_API_KEY='abc'
```

Run server
```sh
uvicorn main:app --reload
```