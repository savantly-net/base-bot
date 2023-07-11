# Pinecone Example

This example uses pinecone to store the vectors.  
It also provides a simple ingest script to load data from the docs folder into pinecone.  

## Quick start

Create an index on pinecone that has `1536` dimensions.  

Use the `sample.env` to create a `.env` file with the correct values.  
Place your documents into the `docs` subfolder.  

Then - 

```shell
make start
```

This will build a local docker image and startup the server on port 9000