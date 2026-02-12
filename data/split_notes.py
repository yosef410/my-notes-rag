# Read your notes file
with open('data/notes.py', 'r') as f:
    content = f.read()

# Split by "#day" or "# day"
parts = content.replace('# day', '#day').split('#day')

# Create documents list
documents = []
for i, part in enumerate(parts):
    if part.strip():
        documents.append({
            "day": i,
            "content": part.strip()[:1000]  # First 1000 chars
        })

print(f"Created {len(documents)} documents")

# Show first 3
for doc in documents[:3]:
    print(f"\n--- Day {doc['day']} ---")
    print(doc['content'][:200] + "...")
