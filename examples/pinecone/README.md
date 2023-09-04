# Pinecone Example

This example uses pinecone to store the vectors.  
It also provides a simple ingest script to load data from the docs folder into pinecone.  

## Quick start

First, create an index on pinecone that has `1536` dimensions.  

Then, use the `sample.env` to create a `.env` file with the correct values.  
Place your documents into the `docs` subfolder.  

To ingest your documents into Pinecone -  

```shell
make ingest
```

To start the bot - 

```shell
make start
```

This will startup the server on port 9000