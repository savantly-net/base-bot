# Overrides base-bot Example

Creates a custom Docker image based on the `savantly/base-bot` image.  
Adds additional python packages and custom implementations.  

The `docker-compose.yml` mounts the [custom files](./custom/)  in the docker image.  

The [data/stores](./data/stores/) directory is mounted for vector store persistence between restarts.  

Specifically, this example uses Google Drive as the document source.   

## Quick start

- Enable Google Drive API access and store your credentials like this [credentials.json](example.credentials.json)  
  More information - https://python.langchain.com/docs/modules/data_connection/document_loaders/integrations/google_drive  
- Have your OPENAI_API_KEY exported as an ENV var.   
- Replace the Google Drive folder ID in [ingest.py](ingest.py) 
- Install the Google dependencies
- Run the ingest process
- Start Docker Compose


```shell
export OPENAI_API_KEY=xxxxxxx
pip install -r requirements.txt
docker-compose up
```

Then open your browser to [http://localhost:9000](http://localhost:9000)  

