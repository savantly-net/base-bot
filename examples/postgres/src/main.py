from flask import Flask, request, jsonify
from langchain.document_store.sql import SQLDocumentStore
from langchain.query import Query
import psycopg2

app = Flask(__name__)

def init_document_store():
    return SQLDocumentStore(url="postgresql://bot_user:bot_password@localhost:5432/bot_database")

def seed_database():
    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        dbname="bot_database",
        user="bot_user",
        password="bot_password"
    )
    cur = conn.cursor()
    with open("data/example_data.sql", "r") as file:
        sql_script = file.read()
        cur.execute(sql_script)
    conn.commit()
    conn.close()

def process_query(query_text):
    document_store = init_document_store()
    query = Query(query_text)
    results = document_store.query(query)
    return results

@app.route("/query", methods=["POST"])
def query():
    data = request.json
    query_text = data["query"]
    results = process_query(query_text)
    return jsonify(results)

if __name__ == "__main__":
    seed_database()
    app.run(host="0.0.0.0", port=8000)
