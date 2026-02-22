from search.search import search
from api.claude import ask_cloude
from utils.logger import log
history = []

log("APP started")

print("chat here (type 'quit' to exit)")
print("-" * 40)


while True:

     qustion = input("\nYou:  ")

     if qustion.lower() == "quit":
        log("User quit")
        print("goodbye!")
        break

     log(f"User asks: {qustion}")
     docs = search(qustion)

     log(f"Found {len(docs)} documents")
     history.append({"role": "user","content": qustion})

     answer = ask_cloude(qustion, docs, history)

     log(f"Got response from claude")
     history.append({"role":"assistant", "content": answer})

     print(f"\nAssistant: {answer}")
