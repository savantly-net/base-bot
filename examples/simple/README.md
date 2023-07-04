# Simple base-bot Example

The `docker-compose.yml` mounts the [data/docs](./data/docs/) folder inside the base-bot image.  

The domain specific data is read from the [data/docs](./data/docs/) folder when the application starts.  

The [data/stores](./data/stores/) directory is mounted for vector store persistence between restarts.  


## Run

```
export OPENAI_API_KEY=xxxxxxx
docker-compose up
```

Then open your browser to [http://localhost:9000](http://localhost:9000)  

