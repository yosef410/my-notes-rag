import sqlite3
import json
import os
import time
import voyageai
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
voyage = voyageai.Client(api_key=os.getenv('VOYAGE_API_KEY'))

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

# Create vectors using Voyage AI (in batches)
texts = [doc['content'] for doc in documents]
vectors = []

print("Creating embeddings (this takes ~20 min, please wait)...")
batch_size = 2

for i in range(0, len(texts), batch_size):
    batch = texts[i:i + batch_size]
    print(f"Processing {i+1}-{i+len(batch)} of {len(texts)}...")
    
    result = voyage.embed(batch, model="voyage-3-lite")
    vectors.extend(result.embeddings)
    
    if i + batch_size < len(texts):
        time.sleep(25)

# Save each document with vector
for i, doc in enumerate(documents):
    vector_text = json.dumps(vectors[i])
    cursor.execute('INSERT INTO documents (day, content, vector) VALUES (?, ?, ?)',
        (doc['day'], doc['content'], vector_text))

connection.commit()
connection.close()
print(f"Saved {len(documents)} documents to database!")
