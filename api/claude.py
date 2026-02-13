import requests
import os
from  dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('cloude_1')

def ask_cloude(ask, docs):
    url = "https://api.anthropic.com/v1/messages" 
    headers = {
          "x-api-key": api_key,
        "anthropic-version": "2023-06-01",
        "content-type": "application/json"
    }
    docs_text = "\n\n".join([d["content"]for d in docs])

    prompts = f"""Here are some notes:

{docs_text}

Based on those notes, answer this qustion: {ask}
"""
    data = {
        "model": "claude-sonnet-4-20250514",
        "max_tokens": 500,
        "messages": [{"role": "user", "content": prompts}]
    }

    requess = requests.post(url, headers=headers, json=data)

    if requess.status_code == 200:
       return requess.json()['content'][0]['text']
    else:
       return f"error: {requess.status_code}"

