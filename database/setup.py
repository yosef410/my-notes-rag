import sqlite3
import json
import voyageai
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
VOYAGE_API_KEY = os.getenv('VOYAGE_API_KEY')

# Setup Voyage client
voyage = voyageai.Client(api_key=VOYAGE_API_KEY)

# Setup database
connection = sqlite3.connect('database/notes.db')
cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS documents (
    id INTEGER PRIMARY KEY,
    day INTEGER,
    content TEXT,
    vector TEXT
)''')
connection.commit()

# Read your notes
with open('data/notes.py', 'r') as f:
    content = f.read()

parts = content.replace('# day', '#day').split('#day')

documents = []
for i, part in enumerate(parts):
    if part.strip():
        documents.append({
            "day": i,
            "content": part.strip()[:3000]
        })

print(f"Found {len(documents)} documents")

# Create vectors using Voyage AI
texts = [doc['content'] for doc in documents]

print("Creating embeddings with Voyage AI...")
result = voyage.embed(texts, model="voyage-3-lite")
vectors = result.embeddings

# Save each document with vector
for i, doc in enumerate(documents):
    vector_text = json.dumps(vectors[i])
    cursor.execute('INSERT INTO documents (day, content, vector) VALUES (?, ?, ?)',
        (doc['day'], doc['content'], vector_text))

connection.commit()
connection.close()
print(f"Saved {len(documents)} documents to database!")
