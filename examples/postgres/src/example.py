import os
from typing import List, Dict
import psycopg2

from langchain.base_bot import BaseBot, Document, BaseBotConfig


class PostgreSQLBot(BaseBot):
    def __init__(self, config: BaseBotConfig):
        super().__init__(config)

    def get_documents(self) -> List[Document]:
        connection = psycopg2.connect(
            host=self.config.postgres_host,
            port=self.config.postgres_port,
            database=self.config.postgres_db,
            user=self.config.postgres_user,
            password=self.config.postgres_password,
        )

        cursor = connection.cursor()
        cursor.execute("SELECT * FROM documents;")
        rows = cursor.fetchall()

        documents = []
        for row in rows:
            doc_id, text, title = row
            documents.append(Document(id=doc_id, text=text, title=title))

        cursor.close()
        connection.close()

        return documents


def main():
    bot_config = BaseBotConfig.from_env()
    bot = PostgreSQLBot(bot_config)
    bot.run()


if __name__ == "__main__":
    main()
