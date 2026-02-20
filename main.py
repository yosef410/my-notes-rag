from search.search import search
from api.claude import ask_cloude

history = []

print("chat here (type 'quit' to exit)")
print("-" * 40)


while True:

     qustion = input("\nYou:  ")

     if qustion.lower() == "quit":
        print("goodbye!")
        break

     docs = search(qustion)

     history.append({"role": "user","content": qustion})

     answer = ask_cloude(qustion, docs)

     history.append({"role":"assistant", "content": answer})

     print(f"\nAssistant: {answer}")
