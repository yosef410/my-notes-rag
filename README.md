# my notes with rag


we use rag to let him see the all of my notes 
## what dose we doing

 
we create the progect when we heve qustion about the diffrent things about the notse the and when it asked by the model i will get the input + the documants (notes) then will answer based 
of it with using rag its help us not only to choose the exect subject but by the meaning with(rag)
# how dose it work

 
- **voyage**- for the embedding model in the db(vectors)
-**sqlite** - for the data base 
- **claude api ** - for the api model ai answer 
#setup


we create rapo with venv(vertual enviroment
 Create virtual environment: `python3 -m venv venv`
 Activate it: `source venv/bin/activate`
 install the packages `pip install -r requirements.txt`
 and put the api keys and project companeys in .env
 VOYAGE_API_KEY=your_key_here
 CLAUDE_API_KEY=your_key_here
 then we run python3 main.py

#files


- `main.py` - runs the RAG system
- `search/search.py` - vector search function
- `api/claude.py` - Claude API connection
- `database/setup.py` - creates embeddings and database
- `data/notes.py` - 170 days of learning notes

## Built by

the small me 
