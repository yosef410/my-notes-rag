import sqlite3
import json
import math
import voyageai
import os
from dotenv import load_dotenv

load_dotenv()
voyage = voyageai.Client(api_key=os.getenv('VOYAGE_API_KEY'))

def distance(vec1, vec2):
    total = 0
    for w in range(len(vec1)):
        minus = vec1[w] - vec2[w]
        total += minus * minus
    return math.sqrt(total)
def search(query, top=3):

    vector = voyage.embed([query], model="voyage-3-lite")
    text_vector = vector.embeddings[0]

    connection =sqlite3.connect('database/notes.db')
    cursor = connection.cursor()

    cursor.execute('SELECT day, content, vector FROM documents')

    pro = []
    for x in cursor.fetchall():
        doc_vector = json.loads(x[2])
        dist = distance(text_vector, doc_vector)

        pro.append({"day": x[0],
                    "content": x[1][:200] ,
                    "distance": dist
        })

    pro.sort(key=lambda z: z["distance"])
    connection.close()
    return pro[:top]


if __name__ == "__main__":
    query = "how do loop work"
    print(f"searching: {query}\n")
    for r in search(query):
        print(f"day {r['day']} (distance: {r['distance']:.3f}")
        print(f"{r['content']}...")
        print()
