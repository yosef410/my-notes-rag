from search.search import search
from api.claude import ask_cloude

qustion = input("Ask about your notes: ")

docs = search(qustion)


answer = ask_cloude(qustion, docs)

print(answer)
