# Savantly base-bot

This is a chat bot based on the LangChain chat bot, packaged up and parameterized for easy re-use.  
The app leverages LangChain's streaming support and async API to update the page in real time for multiple users.  

You can run the docker container with mounted volumes to modify the default behavior.   

## TLDR;
Run in docker (requires your OPENAI_API_KEY as an env variable)  
```shell
docker run -p 9000:9000 -e OPENAI_API_KEY=${OPENAI_API_KEY} savantly/nexus-bot
```

![screenshot](./docs/screenshot.png)

## ✅ Running locally
1. Install dependencies: `pip install -r requirements.txt`
1. Run `ingest.sh` to ingest LangChain docs data into the vectorstore (only needs to be done once).
   1. You can use other [Document Loaders](https://langchain.readthedocs.io/en/latest/modules/document_loaders.html) to load your own data into the vectorstore.
1. Run the app: `make start`
   1. To enable tracing, make sure `langchain-server` is running locally and pass `tracing=True` to `get_chain` in `main.py`. You can find more documentation [here](https://langchain.readthedocs.io/en/latest/tracing.html).
1. Open [localhost:9000](http://localhost:9000) in your browser.


## Configuration 
Modify the `settings.py` to customize the chat parameters.  
Add a `.secrets.py` file to hold your secret data.  

Both of these files can be mounted in place if you're using the pre-built Docker image.  


## 📚 Technical description

There are two components: ingestion and question-answering.

Ingestion has the following steps:

1. Scan the `./data/docs` folder for content to load. The scan ignores any files that begin with a dot.  
2. Load the documents with LangChain's DirectoryLoader.  
3. Split documents with LangChain's [TextSplitter](https://langchain.readthedocs.io/en/latest/reference/modules/text_splitter.html)
4. Create a vectorstore of embeddings, using LangChain's [vectorstore wrapper](https://python.langchain.com/en/latest/modules/indexes/vectorstores.html) (with OpenAI's embeddings and FAISS vectorstore).

Question-Answering has the following steps

1. Given the chat history and new user input, determine what a standalone question would be (using GPT-3).
2. Given that standalone question, look up relevant documents from the vectorstore.
3. Pass the standalone question and relevant documents to GPT-3 to generate a final answer.


## Roadmap

- [x] Parameterize prompts and ingestion settings
- [x] Enable loading docs from a folder
- [x] Create Docker image
- [ ] Create parameters and code to substitute the pickled vector store for Pinecone
- [ ] Create Helm chart
- [ ] Create web-component for dropping the chat on any web page 
- [ ] Parameterize additional chain settings??
