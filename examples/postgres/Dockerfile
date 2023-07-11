FROM savantly/base-bot:latest

COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

#COPY data/stores/vectorstore.pkl /app/data/stores/vectorstore.pkl

COPY src/vectorstore.py /app/base_bot/vectorstore.py
COPY src/settings.py /app/settings.py
